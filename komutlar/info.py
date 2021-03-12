import platform
import random
import discord
from discord import Embed
from discord.ext import commands



class info(commands.Cog):
    @commands.command(name='bot', aliases=["botbilgi", "botinfo"], description='Bot istatislik')
    async def stats(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(ctx.bot.guilds)
        memberCount = len(set(ctx.bot.get_all_members()))
        embed = discord.Embed(title=f'{ctx.bot.user.name} İstatislik', description='\uFEFF', colour=ctx.author.colour)
        embed.add_field(name='Bot Version:', value="2.1.0")
        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Botun olduğu sunucu:', value=serverCount)
        embed.add_field(name='Toplam Üye:', value=memberCount)
        embed.add_field(name='Bot Yapımcısı:', value="<@721798616200773722>")
        embed.set_footer(text=f"Bot adı | {ctx.bot.user.name}")
        embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="invite", aliases=["davet"])
    async def botinvite(self, ctx):
        serverCount = len(ctx.bot.guilds)

        embed = discord.Embed(title=f'Bot Davet {ctx.bot.user.name}', description="\uFEFF", colour=random.randint(0, 0xFFFFFF))
        embed.add_field(name="Bot davet;", value="[Bot daveti için tıkla](https://discord.com/api/oauth2/authorize?client_id=784141794153332786&permissions=8&scope=bot)", inline=False)
        embed.add_field(name="Bot yapımcısının sunucusu;", value=f"[Sunucu için tıkla](https://discord.gg/TTCuZYQFVy)", inline=False)
        embed.add_field(name='Botun olduğu sunucu:', value=serverCount, inline=False)
        embed.add_field(name='Bot Yapımcısı:', value="<@721798616200773722>", inline=False)
        embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar_url)

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(info())