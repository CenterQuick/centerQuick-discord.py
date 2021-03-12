import discord
from discord.ext import commands, tasks
from discord import message, Embed
from discord.utils import get
import json
import os
import random

from io import BytesIO

from PIL import Image, ImageDraw, ImageFont, ImageColor

class cqnomy(commands.Cog):

    @commands.command(name="cüzdanoluştur", aliases=["co", "createwallet", "cw"])
    async def wallet(self, ctx):
        F = open("./data/coin.json", "r+")
        coin = json.load(F)

        if str(f"{ctx.author.id}") in coin:
            await ctx.channel.send(f"{ctx.author.mention} Kullanıcıya ait bir cüzdan bulunmakta.")
            return

        if str(f"{ctx.author.id}") not in coin:
            coin[f"{ctx.author.id}"] = {
                "coin" : "100"
            }

            F.close()

            await ctx.channel.send(f"{ctx.author.mention} Kullanıcı cüzdanı oluşturuldu.")

        with open("./data/coin.json", "r+") as fw:
            json.dump(coin, fw)


    @commands.command(name="para", aliases=["cüzdan", "money", "wallet"])
    async def balance(self, ctx):
        with open("./data/coin.json", "r") as f:
            coin = json.load(f)

        if f"{ctx.author.id}" not in coin:
            await ctx.send(f"{ctx.author.mention} Kullanıcı cüzdanı bulunmamakta.")

        else:
            money = coin[f"{ctx.author.id}"]["coin"]

            embed = discord.Embed(title="Kullanıcı Cüzdanı", description="", color=random.randint(0, 0xFFFFFF))
            embed.add_field(name="Para Miktarı", value="--- " + money + " ---")
            embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)

            await ctx.channel.send(embed=embed)

        f.close()
            

        
    
def setup(bot):
    bot.add_cog(cqnomy())