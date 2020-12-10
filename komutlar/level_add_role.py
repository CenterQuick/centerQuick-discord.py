import discord
from discord.ext import commands, tasks
from discord import message
from discord import Member
from discord.utils import get
import json
import os



class levelrole(commands.Cog):

    @commands.Cog.listener()
    async def  on_message(self, ctx):
        F = open("./data/users.json", "r+")

        lvl = json.load(F)

        LVL = lvl[f"{ctx.guild.id}"][f"{ctx.author.id}"]["level"]

        lvl1 = get(ctx.guild.roles, name="1.Seviye")
        lvl2 = get(ctx.guild.roles, name="2.Seviye")
        lvl3 = get(ctx.guild.roles, name="3.Seviye")
        lvl4 = get(ctx.guild.roles, name="4.Seviye")
        lvl5 = get(ctx.guild.roles, name="5.Seviye")
        lvl6 = get(ctx.guild.roles, name="6.Seviye")
        lvl7 = get(ctx.guild.roles, name="7.Seviye")
        lvl8 = get(ctx.guild.roles, name="8.Seviye")
        lvl9 = get(ctx.guild.roles, name="9.Seviye")
        lvl10 = get(ctx.guild.roles, name="10.Seviye")

        if LVL == "2":
            await ctx.author.add_roles(lvl2)
            await ctx.author.remove_roles(lvl1)

        if LVL == "3":
            await ctx.author.add_roles(lvl3)
            await ctx.author.remove_roles(lvl2)

        if LVL == "4":
            await ctx.author.add_roles(lvl4)
            await ctx.author.remove_roles(lvl3)

        if LVL == "5":
            await ctx.author.add_roles(lvl5)
            await ctx.author.remove_roles(lvl4)

        if LVL == "6":
            await ctx.author.add_roles(lvl6)
            await ctx.author.remove_roles(lvl5)

        if LVL == "7":
            await ctx.author.add_roles(lvl7)
            await ctx.author.remove_roles(lvl6)
        
        if LVL == "8":
            await ctx.author.add_roles(lvl8)
            await ctx.author.remove_roles(lvl7)

        if LVL == "9":
            await ctx.author.add_roles(lvl9)
            await ctx.author.remove_roles(lvl8)

        if LVL == "10":
            await ctx.author.add_roles(lvl10)
            await ctx.author.remove_roles(lvl9)
            


        F.close()

def setup(bot):
    bot.add_cog(levelrole())