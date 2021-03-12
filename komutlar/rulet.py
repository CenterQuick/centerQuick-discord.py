import random
import asyncio

import discord

from discord.ext import commands
from discord import Embed
from discord import Member

class duelrulet(commands.Cog):
    @commands.command(name="duello", aliases=["rusrulet","rulet"])
    async def rusrulet(self, ctx, member : discord.Member):
        if len(ctx.message.mentions) != 1:
            await ctx.send(f"Lütfen bu şekilde kullanınız: `?duello @isim`")
        else:
            await ctx.channel.send("Duelloyu kabul etmek için: `kabul` \nRed etmek için: `iptal` \n**Küçük harf olmasına dikkat ediniz**")
            bekle = await ctx.bot.wait_for('message')
            guess = str(bekle.content)
            
            if guess == "kabul":
                await ctx.channel.send("**Herkez 3 kere sıkar, Ölmeyen kazanır.**")
                await asyncio.sleep(3)

                liste = "Boş", "Boş", "Boş", "Boş", "Dolu"
                for i in range(0, 3):
                    await asyncio.sleep(2)
                    s1 = random.choice(liste)
                    await ctx.send(f"{ctx.author.mention} Sıktı, {s1} geldi.")
                    if s1 == "Dolu":
                        await ctx.send(f"{ctx.author.mention} Kaybetti.")
                        break
                for x in range(0, 3):
                    await asyncio.sleep(2)
                    s2 = random.choice(liste)
                    await ctx.send(f"{member.mention} Sıktı, {s2} geldi.")
                    if s2 == "Dolu":
                        await ctx.send(f"{member.mention} Kaybetti.")
                        break
            else:
                await ctx.channel.send("**KORKAK TAVUK** \n**DUELLOYU RED ETTİ.**")


def setup(bot):
    bot.add_cog(duelrulet())