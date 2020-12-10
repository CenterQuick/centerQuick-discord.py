import aiohttp
import urllib
import random
import discord
from discord.ext import commands
from discord import Embed

kahve = [
    'https://i.pinimg.com/originals/0e/8d/52/0e8d52e8206c524576bb8d14224276a5.gif',
    'https://i.pinimg.com/originals/f2/ca/a8/f2caa8a899298d7d318eaeff94d6881f.gif',
    'https://media1.tenor.com/images/47bc3e68fdedb1867d249ccc0adbee73/tenor.gif?itemid=10745813',
    'https://usercontent.one/wp/www.kircicekleri.com/wp-content/grand-media/image/kahve_1.gif'
]

kedi = [
    'https://img-s1.onedio.com/id-54137d8099c5fa5a06d733ce/rev-0/w-500/s-f8d60adfd93220ff7250355d90309cca2667d717.gif',
    'https://media2.giphy.com/media/hI9rLzJoiL12o/giphy.gif',
    'https://media.tenor.com/images/c50ca435dffdb837914e7cb32c1e7edf/tenor.gif',
    'https://25.media.tumblr.com/a6aedf7dd3a900038b29e24b790acd39/tumblr_mkchovajuW1rx5gpqo6_500.gif',
    'https://data.whicdn.com/images/327564399/original.gif',
    'https://64.media.tumblr.com/9005f506c900f50207841250aeb1d4f4/tumblr_n3at3fXzlS1s3iudgo1_400.gifv'
]

köpek = [
    'https://66.media.tumblr.com/50ee53c5b1798b015a4909ab70ea2321/ab807d6646c7a725-c1/s500x750/caaf3fea69afa6ea3ccd91f414b8ca8a1c81bdc6.gif',
    'https://64.media.tumblr.com/35d41558da0b5b077a18596ad1de4072/tumblr_om31y2On1H1v33e53o1_400.gifv',
    'https://media1.tenor.com/images/602dbd1e79d97efa83e77541ad19f52c/tenor.gif?itemid=10574096',
    'https://49.media.tumblr.com/0f4570242d4cfd18a4d4218414d593e7/tumblr_o4kowsE7Sf1u4nbmvo1_400.gif',
    'https://media1.tenor.com/images/5c800faba9d3cd440d3d92eb7fdf5c26/tenor.gif?itemid=10574056',
    'https://i.pinimg.com/originals/3b/39/0f/3b390f11d3adf4183455c4842c11fe6b.gif'
]

hug = [
    'https://media.tenor.com/images/afbc39fcc4cbe67d9622f657d60d41cf/tenor.gif',
    'https://media3.giphy.com/media/B57QUGJJFfft6/200.gif',
    'https://media2.giphy.com/media/cNwi7weKS4Hg3Y9Wgu/200.gif',
    'https://i.pinimg.com/originals/c7/d6/40/c7d64069782147c69696d9acd81c6da9.gif',
    'https://i.gifer.com/origin/59/59946f2e3c7dea88076eab7a8728aca1_w200.gif',
    'https://media1.tenor.com/images/022a19f8ad9260b5045e16289e66c903/tenor.gif?itemid=7484223'
]

tokat = [
    'https://i.pinimg.com/originals/c0/29/e7/c029e7cebdf632468e35ab903d1b331e.gif',
    'https://media1.tenor.com/images/b980428d9ab96cc24e690ec9b00a783f/tenor.gif?itemid=7205678',
    'https://4.bp.blogspot.com/-WfzGkNhjFIE/Vi-vwoWklXI/AAAAAAAAPCc/HXSnXtEMGs0/w680/kemal_sunal_sener_sen_tokat.gif',
    'https://media0.giphy.com/media/J07H1nnjD6I6i18ouB/200.gif',
    'https://fikircok.net/wp-content/uploads/tokat-atan-alarm.gif',
    'https://j.gifs.com/y46XdJ.gif'
]


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def yaz(self,ctx, *,string):
        await ctx.message.delete()
        await ctx.send(string)

    @commands.command(name="yazdır")
    async def embedsay(self, ctx, *, message):
        await ctx.message.delete()
        em = discord.Embed(color=random.randint(0, 0xFFFFFF))
        em.description = message
        await ctx.send(embed=em)

    @commands.command(aliases=["table", "flip"])
    async def fırlat(self, ctx):
        """Throw a table in anger."""
        await ctx.send("```(╯°□°)╯︵ ┻━┻```")

    @commands.command(name="kedi")
    async def cat(self, ctx):
        await ctx.send(random.choice(kedi))

    @commands.command(name="köpek")
    async def dog(self, ctx):
        await ctx.send(random.choice(köpek))

    @commands.command(name="kahve")
    async def coffee(self, ctx):
        await ctx.send(random.choice(kahve))

    @commands.command(name="sarıl")
    async def hug(self, ctx):
        pass
        if len(ctx.message.mentions) != 1:
            await ctx.send(f"Lütfen bu şekilde kullanınız: `?sarıl @isim`")
        else:
            user = ctx.message.mentions[0]

            hug2 = random.choice(hug)
            embed = discord.Embed(title="", description=f"{user.mention}'a sarılıyor.", color=random.randint(0, 0xFFFFFF))
            embed.set_image(url=hug2)

            await ctx.send(embed=embed)

    @commands.command(name="tokat")
    async def slap(self, ctx):
        pass
        if len(ctx.message.mentions) != 1:
            await ctx.send(f"Lütfen bu şekilde kullanınız: `?tokat @isim`")
        else:
            user = ctx.message.mentions[0]

            tokat2 = random.choice(tokat)
            embed = discord.Embed(title="", description=f"{user.mention}'a tokat atıyor.", color=random.randint(0, 0xFFFFFF))
            embed.set_image(url=tokat2)

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))