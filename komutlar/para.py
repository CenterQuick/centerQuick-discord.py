import discord
from discord.ext import commands
from discord import Embed
import random

parayuzu = [
    "Yazı",
    "Tura"
]

class yazıtura(commands.Cog):

    @commands.command(name="yazıtura")
    async def paraat(self, ctx):
        s1 = random.choice(parayuzu)

        embed = discord.Embed(title="Para atıldı", description="")
        embed.add_field(name="atıldı", value=s1 + " geldi.")
        embed.set_image(url="https://img-s2.onedio.com/id-55507ad8515ad85a60a58271/rev-0/w-300/h-257/f-gif/s-231c62beb8937c9ff986552172628e84332bf6c2.gif")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(yazıtura())