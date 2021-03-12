import random
import asyncio
import discord

from discord.ext import commands
from discord import Embed

verblist = [
    "Evet",
    "Hayır",
    "Belki",
    "Kesinlikle",
    "Kuşkusuz",
    "Bana güvenebilirsin",
    "Şimdi söylememek daha iyi",
    "Konstre ol ve tekrar sor",
    "Dışarıdan iyi görünüyor",
    "Büyülü kaynaklarım olumlu diyor",
    "Büyülü kaynaklarım olumsuz diyor",
    "İyi görünüyor",
    "Kulağa hoş geliyor.",
    "Şüpheli",
    "Çok şüpheli",
    "Git burdan! Şu anda çalışıyorum.",
    "Biraz belirsiz tekrar dene",
    "Şimdi kehanette bulunamam.",
    "Pek iyi görünüyor",
    "Büyük ihtimalle"
]

links = [
    "https://thumbs.gfycat.com/RingedFarawayCricket-max-1mb.gif",
    "https://i.pinimg.com/originals/4d/ca/d9/4dcad98ff2d9aba671b56957ab5d70a2.gif",
    "https://i.pinimg.com/originals/45/df/08/45df08b11e6cb24add4cf1b77a50620e.gif",
    "https://i.gifer.com/3Qqj.gif",
    "https://media.tenor.com/images/e8bb0cdcc320d38daad544cdd78c1f1a/tenor.gif",
    "https://38.media.tumblr.com/7882fd926bc2560f85ff492fac14ccdf/tumblr_n7l8qj0V9a1ttqmf2o1_500.gif",
    "https://cdn.lowgif.com/full/aaece522cb66c4b8-sacred-geometry-gifs-geometr-a-sagrada-pinterest-oc-and.gif"
]

class ball8(commands.Cog):

    @commands.command(name="sor")
    async def ball_8(self, ctx, *, message):
        sans = random.choice(verblist)
        links2 = random.choice(links)

        embed = discord.Embed(title="Kehanet!", description="", color=random.randint(0, 0xFFFFFF))
        embed.add_field(name="Sorduğun soru", value=message)
        embed.add_field(name="Cevabım", value=sans)
        embed.set_image(url=links2)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ball8())