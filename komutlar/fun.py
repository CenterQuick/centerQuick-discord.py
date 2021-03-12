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
    'https://media1.tenor.com/images/022a19f8ad9260b5045e16289e66c903/tenor.gif?itemid=7484223',
    'https://media1.tenor.com/images/b62f047f8ed11b832cb6c0d8ec30687b/tenor.gif?itemid=12668480',
    'https://tenor.com/view/toilet-bound-hanakokun-anime-anime-hug-gif-16831471'
]

tokat = [
    'https://i.pinimg.com/originals/c0/29/e7/c029e7cebdf632468e35ab903d1b331e.gif',
    'https://media1.tenor.com/images/b980428d9ab96cc24e690ec9b00a783f/tenor.gif?itemid=7205678',
    'https://4.bp.blogspot.com/-WfzGkNhjFIE/Vi-vwoWklXI/AAAAAAAAPCc/HXSnXtEMGs0/w680/kemal_sunal_sener_sen_tokat.gif',
    'https://media0.giphy.com/media/J07H1nnjD6I6i18ouB/200.gif',
    'https://fikircok.net/wp-content/uploads/tokat-atan-alarm.gif',
    'https://j.gifs.com/y46XdJ.gif',
    'https://img.wattpad.com/d5e45358b9cddaebeb3228b520f219de7550120e/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f577267357a7343383574463349413d3d2d33342e313436633362653666386136666362623336303231343131333538302e676966'
]

dans = [
    'https://i.pinimg.com/originals/e0/0f/53/e00f538bef44b55164875182aa09a1d1.gif',
    'https://media0.giphy.com/media/46fSE32PJncBh2V7sG/source.gif',
    'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c972a841-3041-40ba-994a-258fe1e5553e/dd80g6u-95ba0a80-b1ac-4c18-ad3a-bb7baf76fd66.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvYzk3MmE4NDEtMzA0MS00MGJhLTk5NGEtMjU4ZmUxZTU1NTNlXC9kZDgwZzZ1LTk1YmEwYTgwLWIxYWMtNGMxOC1hZDNhLWJiN2JhZjc2ZmQ2Ni5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.aZ7xwBWRmuxLNuqcJJldkndMdMa21IgqCsfrRsyNcR8',
    'https://media3.giphy.com/media/f7dofsYKTBzyh6zVEJ/giphy.gif',
    'https://media4.giphy.com/media/6utFOg5PxXbY8wyyDk/giphy.gif',
    'https://tenor.com/view/zero-two-dance-gif-19586642',
    'https://data.whicdn.com/images/207517463/original.gif',
    'https://media.tenor.com/images/7fa3b39ddac5925af0d81aefeeeb3ad4/tenor.gif'
]

kiss = [
    'https://tenor.com/view/couple-kiss-love-hold-passionate-gif-5052769',
    'https://i.pinimg.com/originals/d3/eb/f6/d3ebf6c72b49166687f89109b746c19f.gif',
    'https://i.gifer.com/2q5n.gif',
    'https://i0.wp.com/www.goodmorning-status.com/wp-content/uploads/2020/05/b922a8523eff688ce93a5eef9b903eca.gif?fit=500%2C281&ssl=1',
    'https://lh3.googleusercontent.com/proxy/seMEM5AZ3wisyxM7mOeDnzKp5uOFIUnfqPRjRCPCTWkIZAGzuxniCI0OqW30KsHkB8duKqxZ7MsHQNlvGqhW4zv7lq3DWnY',
    'https://img.wattpad.com/e6d77bcf6ba40fbeeded01520f62c246f511aa39/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f3763314672437944436e595952673d3d2d3732323130373238322e313539376266626164376339373765323132303432333434353135302e676966',
    'https://i2.wp.com/nileease.com/wp-content/uploads/2020/07/319c0b6efc3f9e5701d2fcc22460a81e.gif?fit=500%2C500&ssl=1',
    'https://media0.giphy.com/media/y2Vm8cSRf3Yys/200.gif',
    'https://tenor.com/view/golden-time-anime-kiss-gif-6155657',
    'https://i.pinimg.com/originals/c1/e1/98/c1e198a514380ebc2956734024a815c9.gif'
]


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="yaz")
    async def yaz(self,ctx, *,string):
        await ctx.message.delete()
        await ctx.send(string)

    @commands.command(name="yazdır")
    async def embedsay(self, ctx, *, message):
        await ctx.message.delete()
        em = discord.Embed(color=random.randint(0, 0xFFFFFF))
        em.description = message
        await ctx.send(embed=em)

    @commands.command(name="kedi", aliases=["cat"])
    async def cat(self, ctx):
        kedi2 = random.choice(kedi)

        embed = discord.Embed(title="Kedi", description="", color=random.randint(0, 0xFFFFFF))
        embed.set_image(url=kedi2)

        await ctx.send(embed=embed)

    @commands.command(name="köpek", aliases=["dog"])
    async def dog(self, ctx):
        köpek2 = random.choice(köpek)

        embed = discord.Embed(title="Köpek", description="", color=random.randint(0, 0xFFFFFF))
        embed.set_image(url=köpek2)

        await ctx.send(embed=embed)

    @commands.command(name="kahve")
    async def coffee(self, ctx):
        kahve2 = random.choice(kahve)

        embed = discord.Embed(title="Kahve", description="", color=random.randint(0, 0xFFFFFF))
        embed.set_image(url=kahve2)

        await ctx.send(embed=embed)

    @commands.command(name="sarıl", aliases=["hug"])
    async def hug(self, ctx):
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
        if len(ctx.message.mentions) != 1:
            await ctx.send(f"Lütfen bu şekilde kullanınız: `?tokat @isim`")
        else:
            user = ctx.message.mentions[0]

            tokat2 = random.choice(tokat)
            embed = discord.Embed(title="", description=f"{user.mention}'a tokat atıyor.", color=random.randint(0, 0xFFFFFF))
            embed.set_image(url=tokat2)

            await ctx.send(embed=embed)

    @commands.command(name="dans", aliases=["dance"])
    async def dance(self, ctx):
        dans2 = random.choice(dans)

        embed = discord.Embed(title="Dans", description="", color=random.randint(0, 0xFFFFFF))
        embed.set_image(url=dans2)

        await ctx.send(embed=embed)

    @commands.command(name="öp", aliases=["kiss"])
    async def kissgif(self, ctx):
        if len(ctx.message.mentions) != 1:
            await ctx.send(f"Lütfen bu şekilde kullanınız: `?öp @isim`")
        else:
            user = ctx.message.mentions[0]

            kiss2 = random.choice(kiss)
            embed = discord.Embed(title="", description=f"{user.mention}'a öpüyor.", color=random.randint(0, 0xFFFFFF))
            embed.set_image(url=kiss2)

            await ctx.send(embed=embed)

    @commands.command(name="aşk", aliases=["aşkölçer", "ship"])
    async def ölcer(self, ctx, member : discord.Member):
        if len(ctx.message.mentions) != 1:
            await ctx.send(f"Lütfen bu şekilde kullanınız: `?aşk @isim`")
        if ctx.author.id == 721798616200773722:
            if member.id == 717317491604324383:

                embed = discord.Embed(title="Aşk ölçer", description="", color=random.randint(0, 0xFFFFFF))
                embed.add_field(name="Sevgi yüzdesi", value="%999...", inline=False)
                embed.add_field(name="Aşıklar", value=f"{ctx.author.mention} / {member.mention}", inline=False)
                embed.set_thumbnail(url=ctx.author.avatar_url)

                await ctx.send(embed=embed)
            else:
                sayi = random.randint(0, 100)
            embed = discord.Embed(title="Aşk ölçer", description="", color=random.randint(0, 0xFFFFFF))
            embed.add_field(name="Sevgi yüzdesi", value=f"%{sayi}", inline=False)
            embed.add_field(name="Testi yapanlar", value=f"{ctx.author.mention} / {member.mention}", inline=False)
            embed.set_thumbnail(url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

        if ctx.author.id == 717317491604324383:
            if member.id == 721798616200773722:

                embed = discord.Embed(title="Aşk ölçer", description="", color=random.randint(0, 0xFFFFFF))
                embed.add_field(name="Sevgi yüzdesi", value="%999...", inline=False)
                embed.add_field(name="Aşıklar", value=f"{ctx.author.mention} / {member.mention}", inline=False)
                embed.set_thumbnail(url=ctx.author.avatar_url)

                await ctx.send(embed=embed)
            else:
                sayi = random.randint(0, 100)
            embed = discord.Embed(title="Aşk ölçer", description="", color=random.randint(0, 0xFFFFFF))
            embed.add_field(name="Sevgi yüzdesi", value=f"%{sayi}", inline=False)
            embed.add_field(name="Testi yapanlar", value=f"{ctx.author.mention} / {member.mention}", inline=False)
            embed.set_thumbnail(url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

        else:
            if ctx.author.id == 721798616200773722:
                return
                
            sayi = random.randint(0, 100)
            embed = discord.Embed(title="Aşk ölçer", description="", color=random.randint(0, 0xFFFFFF))
            embed.add_field(name="Sevgi yüzdesi", value=f"%{sayi}", inline=False)
            embed.add_field(name="Testi yapanlar", value=f"{ctx.author.mention} / {member.mention}", inline=False)
            embed.set_thumbnail(url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

    



def setup(bot):
    bot.add_cog(fun(bot))