import asyncio
import random 
import discord

from discord.ext import commands
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord import message
from discord.utils import get

intents = discord.Intents(messages=True, guilds=True)


class msg(commands.Cog):
    async def cog_check(self, ctx):
        return (ctx.author.id == ctx.guild.owner_id)

        # Dm Command
    @commands.command(name="dm", pass_context = True)
    @commands.has_permissions(administrator = True)
    async def dm(self, ctx, member : discord.Member, *, message):
        await member.send(f'{message}')
        await asyncio.sleep(2)
        await ctx.message.delete()
        await ctx.send('**Mesaj Gönderme Başarılı!**')

    # Duyuru Command
    @commands.command(name="duyuru", pass_context = True)
    @commands.has_permissions(administrator = True)
    async def dm_all(self, ctx, *, message):
        if message != None:
            for member in ctx.guild.members:
                try:
                    await member.send(message)
                    await ctx.channel.send("**'" + "Gönderildi" + "' Alıcı: **" + member.name)
                
                except:
                    await ctx.channel.send("**" + " Gönderilemedi '" + "**" + member.name)

        else:
            await ctx.channel.send("Bu komutu kullanamazsın!")




def setup(bot):
    bot.add_cog(msg())