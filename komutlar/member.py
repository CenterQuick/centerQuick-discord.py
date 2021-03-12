import discord
from discord import Embed
from discord.ext import commands
import random

import time

l1 = [
    "https://i.pinimg.com/originals/60/04/30/600430c1d22c731b94cf4e7dae6b398a.gif",
    "https://steamuserimages-a.akamaihd.net/ugc/922543831008219144/3AD9FCC897208D9E0BB8E26247708BEAC66E259A/",
    "https://i.imgur.com/6N8hre4.gif",
    "https://38.media.tumblr.com/cab51a1ca7c93ed6637cac37e6adc149/tumblr_neitigAqpR1raiktro1_500.gif",
    "https://smashinghub.com/wp-content/uploads/2014/08/cool-loading-animated-gif-3.gif",
    "https://i.pinimg.com/originals/05/91/c7/0591c7d9ed972c451f02e9d52199f1d6.gif",
    "https://1.bp.blogspot.com/-fD83LsBz_7M/T_yR8rRfu4I/AAAAAAAABWg/iO1rv3ggabY/s1600/46601c4d963e87777c2b25b17bdaf9a5dd47dfed_m.gif"
    ]   


class MemberCommands(commands.Cog):
    @commands.command(name="yardım", aliases=["help", "h", "H"])
    async def help(self, ctx):
        embed = discord.Embed(title='CenterQuickBot Help.', description="", color = 0xfffcfc)
        embed.add_field(name="Üye komutları", value = "`avatar` | `profil` | `sunucu`\n`yaz` | `yazdır` | `uyarılar`", inline=False)
        embed.add_field(name="Moderation Module", value="`kick` | `ban` | `dm`\n`duyuru` | `temizle` | `yavaşla`\n`mute` | `unmute` | `uyar`", inline=False)
        embed.add_field(name="Oyunlar", value="`duello` | `tahmin` | `sor`\n`çevir` | `yazıtura`\n`dilek`", inline=False)
        embed.add_field(name="Eğlence komutları", value="`sarıl` | `tokat` | `dans`\n`öp` | `aşk` | `kedi`\n`köpek` | `kahve`", inline=False)
        embed.add_field(name="Ekonomi", value="`cüzdanoluştur` | `cüzdan`", inline=False)
        embed.add_field(name="Bot", value="`botbilgi` | `davet`", inline=False)
        embed.add_field(name="**Prefix**", value="**?**")
        embed.add_field(name="Botu Yapan", value="<@721798616200773722>")
        embed.set_thumbnail(url=ctx.guild.icon_url)
    
        await ctx.send(embed=embed)


    @commands.command(name="avatar", aliases=["a"])
    async def sendUserAvatar(self, ctx):
        if len(ctx.message.mentions) != 1:
            embed = discord.Embed(description=f"{ctx.author.mention}'nın avatarı", color=ctx.author.colour)
            embed.set_image(url=ctx.author.avatar_url)

            await ctx.send(embed=embed)
        else:
            user = ctx.message.mentions[0]
            
            embed = discord.Embed(description=f"{user.mention}'nın avatarı", color=ctx.author.colour)
            embed.set_image(url=user.avatar_url)

            await ctx.send(embed=embed)

    @commands.command(name="profil", aliases=["p"])
    async def sendMemberInfo(self, ctx):
        if len(ctx.message.mentions) != 1:
            await ctx.send("Lütfen bu şekilde kullanınız: `?profil @isim`")
        else:
            user = ctx.message.mentions[0]
            requested_by = ctx.message.author
            
            embed = discord.Embed(title=f"**{user.name}** Member Info", description=f"Member ID | {user.id}", color=0x6675FF)
            embed.set_footer(text=f"Requested by {requested_by.name} | {requested_by.id}")
            embed.set_thumbnail(url=user.avatar_url)

            roles = [role.mention for role in user.roles if not role.name == '@everyone']
            roles_text = " ".join(roles) if roles else user.roles[0].name
            embed.add_field(
                name="Roller",
                value=roles_text,
                inline=False
            )

            j_date = user.joined_at
            embed.add_field(
                name="Katılma Tarihi",
                value=f"{j_date.day}/{j_date.month}/{j_date.year}  {j_date.hour}:{j_date.minute}",
                inline=True,
            )

            c_date = user.created_at
            embed.add_field(
                name="Oluşturma Tarihi",
                value=f"{c_date.day}/{c_date.month}/{c_date.year}  {c_date.hour}:{c_date.minute}",
                inline=True,
            )

            await ctx.send(embed=embed)

    @commands.command(name="sunucu", aliases=["server", "s"])
    async def sendServerInfo(self, ctx):
        embed = discord.Embed(
            title="Sunucu Bilgisi",
            description=f"Kurucu <@{ctx.guild.owner_id}>",
            color=0xEB4334,
        )
        embed.set_footer(text=f"Sunucu İD {ctx.guild.id}")
        embed.set_thumbnail(url=ctx.guild.icon_url)

        online = 0
        offline = 0
        bot = 0
        dnd = 0
        idle = 0

        members = ctx.guild.members
        for m in members:
            if m.bot:
                bot += 1
            elif m.status == discord.Status.online:
                online += 1
            elif (m.status == discord.Status.offline or m.status == discord.Status.invisible):
                offline += 1
            elif m.status == discord.Status.idle:
                idle += 1
            elif m.status == discord.Status.dnd:
                dnd += 1

        embed.add_field(
            name=f"__**{ctx.guild.member_count}** Üyeler__",
            value=f":green_circle: **{online}** Online\n:orange_circle: **{idle}** Idle\n:red_circle: **{dnd}** Busy\n:white_circle: **{offline}** Offline\n:robot: **{bot}** Bot",
            inline=False
        )
        embed.add_field(
            name=f"__**{len(ctx.guild.channels)-len(ctx.guild.categories)}** Kanallar__",
            value=f"Text: **{len(ctx.guild.text_channels)}**\nVoice: **{len(ctx.guild.voice_channels)}**\nKategoriler: **{len(ctx.guild.categories)}**",
            inline=False
        )

        date = ctx.guild.created_at
        embed.add_field(
            name="__Oluşturma Tarihi__",
            value=f"{date.day}/{date.month}/{date.year}  {date.hour}:{date.minute}",
            inline=False
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(MemberCommands())