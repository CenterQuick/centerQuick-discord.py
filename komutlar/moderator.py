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

    # Kick Command
    @commands.command(name="kick")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = "Sebep belirtilmedi!"):
        await member.kick(reason = reason)
        
        embed = discord.Embed(title="CenterQuickBot", description="", colour=random.randint(0, 0xFFFFFF))
        embed.add_field(name="Kullanıcı Atıldı", value=f"{member}' İsimli kullanıcı **Atıldı**", inline=False)
        embed.add_field(name="Atılma Sebebi", value=reason)

        await ctx.send(embed=embed)

    # Ban Command
    @commands.command(name="ban")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = "Sebep belirtilmedi!"):
            await member.ban(reason = reason)

            embed = discord.Embed(title="CenterQuickBot", description="", colour=random.randint(0, 0xFFFFFF))
            embed.add_field(name="Kullanıcı Banlandı", value=f"{member}' İsimli kullanıcı **Banlandı**", inline=False)
            embed.add_field(name="Banlanma Sebebi", value=reason)

            await ctx.send(embed=embed)

    # Clear Chat Command
    @commands.command(name="temizle", aliases=["clear", "sil"])
    @commands.has_permissions(manage_messages = True)
    async def clearMessages(self, ctx, arg):
        deleted = await ctx.channel.purge(limit=int(arg))

        msg = await ctx.send(f"`{len(deleted)}` **Mesajları sildim. Çok kirletme**!")
        await asyncio.sleep(3)
        await msg.delete()

    # Slowmode Command
    @commands.command(name="yavaşla")
    @commands.has_permissions(manage_messages = True)
    async def setSlowmode(self, ctx, delay):
        if delay == "off":
            delay = 0

        await ctx.channel.edit(slowmode_delay = int(delay))

    # Mute Command
    @commands.command(name="mute")
    @commands.has_permissions(kick_members = True)
    async def mute(self, ctx, member: discord.Member):
        try:
            if ctx.message.author.guild_permissions.kick_members:

                muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
                await member.add_roles(muted_role)
                await ctx.send(f"{member} İsimli kullanıcı susturuldu!")

            else:
                await ctx.send("Pardon. Yetkili misin? Ne yapmaya çalışıyorsun!")
        except:
            await ctx.send("**Bot çalışmadı!**")

    # unmute command
    @commands.command(name="unmute")
    @commands.has_permissions(kick_members = True)
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