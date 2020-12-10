import asyncio
import discord
import random

from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord import message
from discord.utils import get

intents = discord.Intents(messages=True, guilds=True)

class ModeratorCommands(commands.Cog):

    async def cog_check(self, ctx):
        moderator = get(ctx.guild.roles, name="Staff")
        return (moderator in ctx.author.roles) or (ctx.author.id == ctx.guild.owner_id)

    # Kick Command
    @commands.command(name="kick")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = "Sebep belirtilmedi!"):
        await member.kick(reason = reason)
        await ctx.send("**Kullanıcı atıldı**")

    # Ban Command
    @commands.command(name="ban")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = "Sebep belirtilmedi!"):
        await member.ban(reason = reason)
        await ctx.send("**Kullanıcı yasaklandı**")

    # Clear Chat Command
    @commands.command(name="temizle")
    async def clearMessages(self, ctx, arg):
        deleted = await ctx.channel.purge(limit=int(arg))

        msg = await ctx.send(f"||{len(deleted)}|| **Mesajları sildim. Çok kirletme**!")
        await asyncio.sleep(3)
        await msg.delete()

    # Dm Command
    @commands.command(name="dm", pass_context = True)
    async def dm(self, ctx, member : discord.Member, *, message):
        await member.send(f'{message}')
        await ctx.send('**Mesaj Gönderme Başarılı!**')

    @commands.command(name="duyuru", pass_context = True)
    async def dm_all(self, ctx, *, message):
        if message != None:
            for member in ctx.guild.members:
                try:
                    await member.send(message)
                    await ctx.channel.send("'" + message + "' Sent to: " + member.name)
                
                except:
                    await ctx.channel.send(" Gönderilemedi '" + "**" + message + "**")

        else:
            await ctx.channel.send("Bu komutu kullanamazsın!")


    # Slowmode Command
    @commands.command(name="yavaşla")
    async def setSlowmode(self, ctx, delay):
        if delay == "off":
            delay = 0

        await ctx.channel.edit(slowmode_delay = int(delay))

    # Mute Command
    @commands.command(name="mute")
    async def mute(self, ctx, member: discord.Member, seconds=None):
        try:
            if ctx.message.author.guild_permissions.kick_members:
                if seconds is None or int(seconds) < 0:
                    
                    await ctx.send("Süreyi Saniye olarak sayı ile belirtiniz.")
                    return
                else:
                    if member.guild_permissions.manage_messages:
                        await ctx.send(f"{member} Kullanıcıyı susturamazsınız. **Yetkiniz yok.**")
                        return

                    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
                    await member.add_roles(muted_role)
                    await ctx.send(f"{member} İsimli kullanıcı `{seconds}` saniye susturuldu!")
                    muted = discord.utils.get(member.roles, name=muted_role)
                    if muted is not None:
                        await asyncio.sleep(int(seconds))
                        await member.add_roles(muted_role)
                        await ctx.send(f"{member} İsimli kullanıcı başarı ile susturuldu!")
            else:
                await ctx.send("Pardon. Yetkili misin? Ne yapmaya çalışıyorsun!")
        except:
            await ctx.send("**Bot çalışmadı!**")

    # unmute command
    @commands.command(name="unmute")
    async def unmute(self, ctx, member : discord.Member):
        try:
            if ctx.message.author.guild_permissions.kick_members:
                muted = discord.utils.get(member.roles, name="Muted")
                if muted is not None:
                    role = discord.utils.get(ctx.guild.roles, name="Muted")
                    await member.remove_roles(role)
                    await member.send("Cezan bitti. Artık konuşabilirsin. Dikkat et yetkilileri kızdırma!")
                    await ctx.send(f"{member} Kullanıcının susturması kaldırıldı!")
                else:
                    await ctx.send(f"{member} Kullanıcı susturulmamış ")
            else:
                await ctx.send("Pardon. Yetkili misin? Ne yapmaya çalışıyorsun!")
            await asyncio.sleep(5)
            await ctx.message.delete()
        except:
            await ctx.send("Sanırım bu komutu kullanamazsın")


def setup(bot):
    bot.add_cog(ModeratorCommands())