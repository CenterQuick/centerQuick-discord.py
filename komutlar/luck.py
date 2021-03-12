import random
import asyncio
import discord

from discord.ext import commands
from discord import Embed

verblist=[
    "Çok şanslısın kuyu seni kabul etti. Dileğin gerçekleşecek.",
    "3 vakte kadar gerçekleşicek.",
    "Dileğinin gerçekleşmesi için lavanta kokla.",
    "Sen kötü birisin dileğin gerçekleşmiycek",
    "**Lanetlendin.**",
    "Dileğin Gerçekleşecek. Ama öldükten sonra.",
    "Dileğine odaklan!"
]

class lucky(commands.Cog):

    @commands.command(name="dilek", aliases=["şans","şanslıkuyu","kuyu","dilekkuyusu"])
    async def luckywater(self, ctx, *, message):
        sans = random.choice(verblist)

        embed = discord.Embed(title="Dilek Kuyusu", description="", color=random.randint(0, 0xFFFFFF))
        embed.add_field(name="Dileğin", value=message, inline=False)
        embed.add_field(name="Cevap", value=sans)
    
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(lucky())