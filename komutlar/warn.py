import discord
import json
import asyncio
import os
import random

from discord.ext import commands
from discord.ext.commands import command, has_permissions
from discord import Embed

os.chdir(r'C:\Users\taha6\Desktop\CQBot')

class warnclass(commands.Cog):
    
    @commands.command(name="uyar", aliases = ["warn"])
    @commands.has_permissions(kick_members = True)
    async def Uyar(self, ctx, member : discord.Member, *, reason = "Sebep belirtilmedi"):
        f = open("./data/warning.json", "r+")
        
        warn = json.load(f)

        if str(f'{ctx.guild.id}') not in warn:
            warn[f'{ctx.guild.id}'] = {}
            print("Uyarı dosyası oluşturuldu!")

        if str(f'{member.id}') not in warn[f'{ctx.guild.id}']:
            warn[f'{ctx.guild.id}'][f'{member.id}'] = {
                "Kullanici" : f"{member.id}", "Uyari Sayisi" : f"0"
            }

        
        WRN = int(warn[f"{ctx.guild.id}"][f"{member.id}"]["Uyari Sayisi"]) + 1

        embed = discord.Embed(title="Kullanıcı Uyarıldı", description=f"{member.mention}", colour=random.randint(0, 0xFFFFFF))
        embed.add_field(name="Uyarılma sebebi", value=reason)
        embed.set_thumbnail(url=member.avatar_url)

        await ctx.send(embed=embed)

        warn[f"{ctx.guild.id}"][f"{member.id}"]["Uyari Sayisi"] = f"{WRN}"
        f.close()

        with open("./data/warning.json", "r+") as fw:
            json.dump(warn, fw)



    @commands.command(name="uyarısayı", aliases=["warns", "warnings", "uyarılar"])
    async def warns(self, ctx, member : discord.Member):
        f = open("./data/warning.json", "r+")
        
        warn = json.load(f)

        if f"{member.id}" not in warn[f"{ctx.guild.id}"]:
            await ctx.channel.send(f"**{member.name}** Kullanıcı daha önce uyarılmamış!")

        else:
            sayi = warn[f"{ctx.guild.id}"][f"{member.id}"]["Uyari Sayisi"]

            await ctx.channel.send(f"**{member.name}** Uyarı sayısı : " + sayi)

        f.close()


def setup(bot):
    bot.add_cog(warnclass())