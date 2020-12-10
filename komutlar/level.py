import discord
from discord.ext import commands, tasks
from discord import message
from discord.utils import get
import json
import os
import random


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



    @commands.command(name="seviye")
    async def level(self, ctx, member : discord.Member = None):
        
        if not member:
            user = ctx.message.author
            with open("./data/users.json", "r") as f:
                users = json.load(f)

            lvl = users[str(ctx.guild.id)][str(user.id)]['level']
            exp = users[str(ctx.guild.id)][str(user.id)]['txp']

            embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP ", color=random.randint(0, 0xFFFFFF))
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

            await ctx.send(embed = embed)

        else:
            with open("./data/users.json", "r") as f:
                users = json.load(f)

            lvl = users[str(ctx.guild.id)][str(member.id)]['level']
            exp = users[str(ctx.guild.id)][str(member.id)]['txp']

            embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP", color=random.randint(0, 0xFFFFFF))
            embed.set_author(name = member, icon_url = member.avatar_url)

            await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(lvlup())