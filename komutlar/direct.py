import discord
import random
import asyncio

from discord.ext import commands, tasks
from discord import Embed
from discord import Message
from discord.utils import get

class DirectMessage(commands.Cog):

    @commands.Cog.listener()
    async def on_dm_messages(self, message):
        print(message)




def setup(bot):
    bot.add_cog(DirectMessage(bot))