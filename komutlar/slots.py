import discord
from discord.ext import commands
from discord import Embed
import random
import asyncio

slot = [
    ":apple:",
    ":lemon:",
    ":strawberry:",
    ":watermelon:",
    ":carrot:",
    ":tangerine:"
]

class slots(commands.Cog):

    @commands.command(name="çevir")
    async def slot(self, ctx):
        s1 = random.choice(slot)
        s2 = random.choice(slot)
        s3 = random.choice(slot)

        if s1 == s2 == s3:
            await asyncio.sleep(3)
            embed = discord.Embed(description="Slot çevirildi!")
            embed.add_field(name="Slotlar", value=s1 + " | " + s2 + " | " + s3)
            embed.add_field(name="Sonuç", value="***KAZANDIN!***")

            await ctx.send(embed=embed)

        else:
            await asyncio.sleep(3)
            embed = discord.Embed(description="Slot çevirildi!")
            embed.add_field(name="Slotlar", value=s1 + " | " + s2 + " | " + s3)
            embed.add_field(name="Sonuç", value="***MAĞLUBİYET!***")

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(slots())