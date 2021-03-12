import asyncio
import discord

from discord.ext import commands


class sesgiris(commands.Cog):
    @commands.command(name="join")
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await ctx.send("Bot ses kanalına girdi!")
        await channel.connect()

    @commands.command(name="leave", pass_context=True)
    async def leave(self, ctx):
        await ctx.send("Bot ses kanalından çıktı!")
        channel = ctx.voice.channel
        await channel.disconnect()


def setup(bot):
    bot.add_cog(sesgiris())