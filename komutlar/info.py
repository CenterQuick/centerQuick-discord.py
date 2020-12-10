import platform
import discord
from discord import Embed
from discord.ext import commands



class info(commands.Cog):
    @commands.command(name='bot', description='Bot istatislik')
    async def stats(self, ctx):
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(ctx.bot.guilds)
        memberCount = len(set(ctx.bot.get_all_members()))
        embed = discord.Embed(title=f'{ctx.bot.user.name} İstatislik', description='\uFEFF', colour=ctx.author.colour)
        embed.add_field(name='Bot Version:', value="1.0.0")
        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Botun olduğu sunucu:', value=serverCount)
        embed.add_field(name='Toplam Üye:', value=memberCount)
        embed.add_field(name='Bot Yapımcısı:', value="<@721798616200773722>")
        embed.set_footer(text=f"Bot adı | {ctx.bot.user.name}")
        embed.set_author(name=ctx.bot.user.name, icon_url=ctx.bot.user.avatar_url)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(info())