import discord
import asyncio
import random
import re
import logging
import functools

import aiohttp

from discord.ext import commands
from discord import Embed
from discord import Message, Member, Guild

class secure(commands.Cog):

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 721798616200773722:
            return
            
        else:
            if message.content in "discord.gg":
                print("Selam !")
                await message.delete()

                embed = discord.Embed(title="REKLAM YAPAMAZSIN !!!", description="", color=random.randint(0, 0xFFFFFF))
                embed.add_field(name=f"{message.author.mention}", value=f"Reklam yapmak yasak!", inline=False)
                
                await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(secure())