import discord
import asyncio

import discord.ext
from discord.ext import commands
from discord.ext.commands import command, has_permissions, bot_has_permissions
from discord.utils import get

class kayıt(commands.Cog):

    @commands.command(name="erkek", aliases=["e"])
    @commands.has_role("Kayıt Görevlisi")
    async def Man(self, ctx, member : discord.Member, name, old):
        man_role = discord.utils.get(ctx.guild.roles, name="Man")
        unregister_role = discord.utils.get(ctx.guild.roles, name="Unregistered")
        pass
        
