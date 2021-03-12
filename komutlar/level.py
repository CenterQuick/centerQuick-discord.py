import discord
from discord.ext import commands, tasks
from discord import message
from discord.utils import get
import json
import os
import random

from io import BytesIO

from PIL import Image, ImageDraw, ImageFont, ImageColor


class lvlup(commands.Cog):

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.content.startswith('B ') is not True:

            if ctx.guild != None:

                F = open("./data/users.json", "r+")

                lvl = json.load(F)


                if str(f'{ctx.guild.id}') not in lvl:
                    lvl[f'{ctx.guild.id}'] = {}
                    print(f"Guild dosyası oluşturuldu : {ctx.guild.id} / {ctx.guild.name}")

                if str(f"{ctx.author.id}") not in lvl[f"{ctx.guild.id}"]:

                    lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"] = {
                        "level" : "1", "xp" : "0", "multi" : f"1", "txp" : f"0"
                        }

                LNum = 1
                MP = int(lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["multi"])
                #XP = int(lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["xp"]) + (LNum * MP)
                TXP = int(lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["txp"]) + (LNum * MP)
                LVL = int(lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["level"])

                if TXP >= LVL * 1000:
                    #XP = XP % (200*(LVL**2))
                    #XP = 1
                    LVL += 1
        

                lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["multi"] = f"{MP}"
                #lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["xp"] = f"{XP}"
                lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["txp"] = f"{TXP}"
                lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["level"] = f"{LVL}"


                F.close()

                with open("./data/users.json", "r+") as fw:
                    json.dump(lvl, fw)

                anlvl = int(lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["level"])
                if anlvl in [800]:
                    print(f"CONGRATS! {ctx.author.mention} has made it to level {anlvl} !")



    @commands.command(name="seviye", aliases=["level", "rank"])
    async def level(self, ctx, member : discord.Member = None):

        if not member:
            if ctx.author.id == 721798616200773722:
                user = ctx.message.author
                with open("./data/users.json", "r") as f:
                    users = json.load(f)

                lvl = users[str(ctx.guild.id)][str(user.id)]['level']
                exp = users[str(ctx.guild.id)][str(user.id)]['txp']

                img = Image.open("cqthyphon.png").convert('RGB')
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Exo2-Black.ttf", 33)

                asset = ctx.author.avatar_url_as(size=128)
                dta = BytesIO(await asset.read())
                pf = Image.open(dta).convert('RGB')

                draw.text((197, 50), f"{user.name}", (20, 255, 200), font=font)
                draw.text((190, 150), "Level : " + lvl, (20, 255, 200), font=font)
                draw.text((190, 200), "Experience : " + exp, (20, 255, 200), font=font)
        
                pf.copy()
                pf.putalpha(128)

                img.paste(pf, (25, 55))

                img.save('member.png')
                await ctx.send(file = discord.File("member.png"))

            if ctx.author.id == 717317491604324383:
                user = ctx.message.author
                with open("./data/users.json", "r") as f:
                    users = json.load(f)

                lvl = users[str(ctx.guild.id)][str(user.id)]['level']
                exp = users[str(ctx.guild.id)][str(user.id)]['txp']

                img = Image.open("cqepic.png").convert('RGB')
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Exo2-Black.ttf", 33)

                asset = ctx.author.avatar_url_as(size=128)
                dta = BytesIO(await asset.read())
                pf = Image.open(dta).convert('RGB')

                draw.text((197, 50), f"{user.name}", (255, 255, 255), font=font)
                draw.text((190, 150), "Level : " + lvl, (255, 255, 255), font=font)
                draw.text((190, 200), "Experience : " + exp, (255, 255, 255), font=font)
        
                pf.copy()
                pf.putalpha(128)

                img.paste(pf, (25, 55))

                img.save('member.png')
                await ctx.send(file = discord.File("member.png"))
                
            else:
                if ctx.author.id == 721798616200773722:
                    return
                if ctx.author.id == 717317491604324383:
                    return
                    
                user = ctx.message.author
                with open("./data/users.json", "r") as f:
                    users = json.load(f)

                lvl = users[str(ctx.guild.id)][str(user.id)]['level']
                exp = users[str(ctx.guild.id)][str(user.id)]['txp']

                img = Image.open("cqmember.png").convert('RGBA')
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Exo2-Black.ttf", 33)

                asset = ctx.author.avatar_url_as(size=128)
                dta = BytesIO(await asset.read())
                pf = Image.open(dta).convert('RGBA')

                draw.text((197, 50), f"{user.name}", (20, 255, 70), font=font)
                draw.text((190, 150), "Level : " + lvl, (20, 255, 70), font=font)
                draw.text((190, 200), "Experience : " + exp, (20, 255, 70), font=font)
        
                pf.copy()
                pf.putalpha(128)

                img.paste(pf, (25, 55))

                img.save('member.png')
                await ctx.send(file = discord.File("member.png"))

        else:
            if member.id == 721798616200773722:
                with open("./data/users.json", "r") as f:
                    users = json.load(f)

                lvl = users[str(ctx.guild.id)][str(member.id)]['level']
                exp = users[str(ctx.guild.id)][str(member.id)]['txp']

                img = Image.open("cqthyphon.png").convert('RGB')
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Exo2-Black.ttf", 33)

                asset = member.avatar_url_as(size=128)
                dta = BytesIO(await asset.read())
                pf = Image.open(dta).convert('RGB')

                draw.text((197, 50), f"{member.name}", (20, 255, 200), font=font)
                draw.text((190, 150), "Level : " + lvl, (20, 255, 200), font=font)
                draw.text((190, 200), "Experience : " + exp, (20, 255, 200), font=font)
        
                pf.copy()
                pf.putalpha(128)

                img.paste(pf, (25, 55))

                img.save('member.png')
                await ctx.send(file = discord.File("member.png"))

            if member.id == 717317491604324383:
                with open("./data/users.json", "r") as f:
                    users = json.load(f)

                lvl = users[str(ctx.guild.id)][str(member.id)]['level']
                exp = users[str(ctx.guild.id)][str(member.id)]['txp']

                img = Image.open("cqepic.png").convert('RGB')
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Exo2-Black.ttf", 33)

                asset = member.avatar_url_as(size=128)
                dta = BytesIO(await asset.read())
                pf = Image.open(dta).convert('RGB')

                draw.text((197, 50), f"{member.name}", (255, 255, 255), font=font)
                draw.text((190, 150), "Level : " + lvl, (255, 255, 255), font=font)
                draw.text((190, 200), "Experience : " + exp, (255, 255, 255), font=font)
        
                pf.copy()
                pf.putalpha(128)

                img.paste(pf, (25, 55))

                img.save('member.png')
                await ctx.send(file = discord.File("member.png"))                

            else:
                with open("./data/users.json", "r") as f:
                    users = json.load(f)

                lvl = users[str(ctx.guild.id)][str(member.id)]['level']
                exp = users[str(ctx.guild.id)][str(member.id)]['txp']

                img = Image.open("cqmember.png").convert('RGBA')
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype("Exo2-Black.ttf", 33)

                asset = member.avatar_url_as(size=128)
                dta = BytesIO(await asset.read())
                pf = Image.open(dta).convert('RGBA')

                draw.text((197, 50), f"{member.name}", (20, 255, 70), font=font)
                draw.text((190, 150), "Level : " + lvl, (20, 255, 70), font=font)
                draw.text((190, 200), "Experience : " + exp, (20, 255, 70), font=font)
        
                pf.copy()
                pf.putalpha(128)

                img.paste(pf, (25, 55))

                img.save('member.png')
                await ctx.send(file = discord.File("member.png"))



def setup(bot):
    bot.add_cog(lvlup())