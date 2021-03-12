import discord
from discord.ext import commands
from discord import Embed
import random
import asyncio
import json

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
    async def slot(self, ctx, msg):
        with open("./data/coin.json", "r+") as f:
            coin = json.load(f)

        MN = int(coin[f"{ctx.author.id}"]["coin"])

        s1 = random.choice(slot)
        s2 = random.choice(slot)
        s3 = random.choice(slot)

        if int(msg) == 0:
            await ctx.channel.send("Lütfen bir sayı değeri giriniz.")
            return

        if s1 == ":watermelon:":
            msg = int(msg)
            MN = int(coin[f"{ctx.author.id}"]["coin"]) + msg * 5

            await asyncio.sleep(1)
            embed = discord.Embed(description="Slot çevirildi!")
            embed.add_field(name="Slotlar", value=s1 + " | " + s1 + " | " + s1, inline=False)
            embed.add_field(name="Sonuç", value=str(msg * 5) + " Kazandın.")

            await ctx.send(embed=embed)
            return

        if s1 == s2:
            msg = int(msg)
            MN = int(coin[f"{ctx.author.id}"]["coin"]) + msg

            await asyncio.sleep(1)
            embed = discord.Embed(description="Slot çevirildi!")
            embed.add_field(name="Slotlar", value=s1 + " | " + s2 + " | " + s2, inline=False)
            embed.add_field(name="Sonuç", value=str(msg) + " Kazandın.")

            await ctx.send(embed=embed)
            return

        if s1 == s2 == s3:
            msg = int(msg)
            MN = int(coin[f"{ctx.author.id}"]["coin"]) + msg * 2

            await asyncio.sleep(1)
            embed = discord.Embed(description="Slot çevirildi!")
            embed.add_field(name="Slotlar", value=s1 + " | " + s2 + " | " + s3, inline=False)
            embed.add_field(name="Sonuç", value=str(msg * 2) + " Kazandın.")

            await ctx.send(embed=embed)
            return

        else:
            msg = int(msg)
            MN = int(coin[f"{ctx.author.id}"]["coin"]) - msg

            await asyncio.sleep(1)
            embed = discord.Embed(description="Slot çevirildi!")
            embed.add_field(name="Slotlar", value=s1 + " | " + s2 + " | " + s3, inline=False)
            embed.add_field(name="Sonuç", value=str(msg) + " Kaybettin")

            await ctx.send(embed=embed)

        coin[f"{ctx.author.id}"]["coin"] = f"{MN}"

        f.close()

        with open("./data/coin.json", "r+") as fw:
            json.dump(coin, fw)



 
def setup(bot):
    bot.add_cog(slots())