import re
import logging
import functools

import aiohttp

from discord.ext import commands
from discord import Member, Message, Guild
from discord import Embed



logger = logging.getLogger(__name__)


class Security(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()
        self.guess_language = guess()

    async def security_check(self, ctx, message: Message):
        """
        Runs security checks on message.
        Some checks can delete the message, so no need to run additional checks if message got deleted.
        :param message: message to run checks on
        """
        if ctx.skip_security(message):
            return

        is_message_deleted = False
        await ctx.deal_with_vulgar_words(message)

        if "https:" in message.content or "http:" in message.content:
            is_message_deleted = await ctx.deal_with_invites(message)

        if len(message.attachments) != 0 and not is_message_deleted:
            is_message_deleted = await ctx.deal_with_attachments(message)

        if not is_message_deleted:
            await ctx.deal_with_long_code(message)

    def skip_security(self, ctx, message: Message) -> bool:
        """
        In which cases we will skip our security check for message.
        :param message: message on which we will potentially run security checks
        :return: bool whether we should skip security checks or not
        """
        if message.guild is None or message.author.bot:
            return True
        elif message.guild.id != constant.tortoise_guild_id:
            return True
        elif not isinstance(message.author, Member):
            return True  # Web-hooks messages will appear as from User even tho they are in Guild.
        elif message.author.guild_permissions.administrator:
            return True
        elif ctx.trusted in message.author.roles:
            return True  # Whitelists the members with Trusted role to prevent unnecessary logging

        return False

    async def deal_with_invites(self, ctx, message: Message) -> bool:
        """
        Checks if the message has any invites that are not for Tortoise guild,
        if so deletes the message.
        Works both with discord.com/invite and discord.gg ,including link shorteners.
        :param message: message to check for Discord invites
        :return: bool, was the passed message deleted or not?
        """
        base_url = re.findall(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",  # Find any url
            message.content
        )

        for invite in base_url:
            # Get the endpoint of that url (for discord invite url shorteners)
            try:
                async with self.session.get(invite) as response:
                    invite = str(response.url)
            except aiohttp.ClientConnectorError:
                # The link is not valid
                continue

            if "discord.com/invite/" in invite or "discord.gg/" in invite:
                if not await self.check_if_invite_is_our_guild(invite, message.guild):
                    # TODO give him warning points etc / send to deterrence channel
                    embed = warning(f"{message.author.mention} You are not allowed to send other server invites here.")
                    await message.channel.send(embed=embed)
                    await message.delete()
                    return True

        # If we've come here we did not delete our message
        return False


    async def deal_with_attachments(self, message: Message) -> bool:
        """
        Will delete message if it has attachment that we don't allow or if it is a
        whitelisted attachment extension it will upload it's content to our pastebin
        and reply with link to it.
        :param message: message to check for attachments
        :return: bool, was the passed message deleted or not?
        """
        reply = None

        for attachment in message.attachments:
            try:
                extension = attachment.filename.rsplit('.', 1)[1]
            except IndexError:
                extension = ""  # file has no extension

            extension = extension.lower()

            if extension in extension_to_pastebin:
                if attachment.size > 4096:
                    reply = (
                        f"It looks like you tried to attach a {extension} file which "
                        f"could be code related but since it's too big in size I will not be uploading it "
                        f"to our pastebin for viewing."
                    )
                else:
                    file_content = await attachment.read()
                    url = await self.create_pastebin_link(file_content)
                    reply = (
                        f"It looks like you tried to attach a {extension} file which is not allowed, "
                        "however since it could be code related you can find the paste link here:\n"
                        f"[**{attachment.filename}** {url}]"
                    )
            elif extension not in allowed_file_extensions:
                reply = (
                    f"It looks like you tried to attach a {extension} file which is not allowed, "
                    "as it could potentially contain malicious code."
                )

            if reply:
                await message.channel.send(f"Hey {message.author.mention}!", embed=warning(reply))
                await message.delete()
                return True

        # If we've come here we did not delete our message
        return False

    async def deal_with_long_code(self, message: Message) -> bool:
        """
        When someone sends long message containing code, bot will delete it and upload message content
        to our pastebin and reply with it's link.
        Guessing is quite CPU intensive so be sure to check it only for long messages (not for each).
        :param message: message to check
        :return: bool, was the passed message deleted or not?
        """
        if len(message.content) <= constants.max_message_length:
            return False

        await message.channel.trigger_typing()
        language = await self.bot.loop.run_in_executor(
            None, functools.partial(self.guess_language.language_name, source_code=message.content)
        )

        if not language:
            return False

        pastebin_link = await self.create_pastebin_link(message.content.encode())
        await message.delete()
        msg = (
            f"Detected a long message containing {language} code.\n"
            f"To improve readability I've uploaded it to our pastebin: {pastebin_link}"
        )
        await message.channel.send(embed=warning(msg))
        return True

    async def create_pastebin_link(self, content: bytes) -> str:
        """Creates link to our Pastebin with passed content."""
        async with self.session.post(url=tortoise_paste_endpoint, data=content) as resp:
            data = await resp.json()
        return f"{tortoise_paste_service_link}{data.get('key')}"

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.security_check(message)

    @commands.Cog.listener()
    async def on_message_edit(self, ctx, msg_before, msg_after):
        if msg_before.content == msg_after.content:
            return

        # Log that the message was edited for security reasons
        msg = (
            f"**Message edited in** {msg_before.channel.mention}\n\n"
            f"**Before:** {msg_before.content}\n"
            f"**After: **{msg_after.content}\n\n"
            f"[jump]({msg_after.jump_url})"
        )
        embed = discord.Embed(msg, msg_before.guild.me)
        embed.set_footer(text=f"Author: {msg_before.author}", icon_url=msg_before.author.avatar_url)
        await ctx.log_channel.send(embed=embed)

        # Check if the new message violates our security
        await ctx.security_check(msg_after)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.content == "":
            return  # if it had only attachment for example

        msg = (
            f"**Message deleted in** {message.channel.mention}\n\n"
            f"**Message: **{message.content}"
        )
        embed = info(msg, message.guild.me, "")
        embed.set_footer(text=f"Author: {message.author}", icon_url=message.author.avatar_url)
        await self.log_channel.send(embed=embed)

    @classmethod
    async def check_if_invite_is_our_guild(cls, full_link: str, guild: Guild):
        guild_invites = await guild.invites()
        for invite in guild_invites:
            if cls.get_invite_link_code(invite.url) == cls.get_invite_link_code(full_link):
                return True
        return False

    @classmethod
    def get_invite_link_code(cls, string: str):
        return string.split("/")[-1]


def setup(bot):
    bot.add_cog(Security(bot))