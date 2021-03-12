import random
import discord

from discord.ext import commands
from discord import message


class pvp(commands.Cog):
    @commands.command(name="düello")
    async def düello(self, ctx, message):
        if len(ctx.message.mentions) != 1:
            await ctx.send(f"Lütfen bu şekilde kullanınız: `?düello @isim`")
        else:
            oyuncu2 = ctx.message.mentions[0]

            oyuncu1 = ctx.message.author
            can1 = 500
            can2 = 500
            saldırı = random.randint(0, 250)
            can3 = 0
            can4 = 0

            



def setup(bot):
    bot.add_cog(pvp())