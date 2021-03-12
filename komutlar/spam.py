import asyncio
import random
import discord

from discord.ext import commands, tasks
from discord import Embed


class spamverbs(commands.Cog):

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.content == "sa":
            if message.author.id == 721798616200773722:
                emoji = "❤️"
            
                embed = discord.Embed(title="", description="", color=random.randint(0, 0xFFFFFF))
                embed.add_field(name="Efsane geldi.", value="Efsaneler efsanesi **Thyphon** geldi.`Hoş geldin!`", inline=False)
                
                await message.channel.send(embed=embed)
                await message.add_reaction(emoji)

            if message.author.id == 465464440452677638:
                emoji = "❤️"

                embed = discord.Embed(title="", description="", color=random.randint(0, 0xFFFFFF))
                embed.add_field(name="Prensiniz geldi.", value=f"Kaçın geliyor gelmekte olan! {message.author.mention}.`Hoş geldin!`", inline=False)
                
                await message.channel.send(embed=embed)
                await message.add_reaction(emoji)

            if message.author.id == 785868634341113876:
                emoji = "❤️"

                embed = discord.Embed(title="", description="", color=random.randint(0, 0xFFFFFF))
                embed.add_field(name="Kraliçeniz geldi.", value=f"Önünde diz çökün {message.author.mention}.`Hoş geldin!`", inline=False)
                
                await message.channel.send(embed=embed)
                await message.add_reaction(emoji)

        if message.content == "Sa":
            if message.author.id == 721798616200773722:
                emoji = "❤️"
            
                embed = discord.Embed(title="", description="", color=random.randint(0, 0xFFFFFF))
                embed.add_field(name="Efsane geldi.", value="Efsaneler efsanesi **Thyphon** geldi.`Hoş geldin!`", inline=False)
                
                await message.channel.send(embed=embed)
                await message.add_reaction(emoji)

            if message.author.id == 465464440452677638:
                emoji = "❤️"

                embed = discord.Embed(title="", description="", color=random.randint(0, 0xFFFFFF))
                embed.add_field(name="Prensiniz geldi.", value=f"Kaçın geliyor gelmekte olan! {message.author.mention}.`Hoş geldin!`", inline=False)
                
                await message.channel.send(embed=embed)
                await message.add_reaction(emoji)

            if message.author.id == 785868634341113876:
                emoji = "❤️"

                embed = discord.Embed(title="", description="", color=random.randint(0, 0xFFFFFF))
                embed.add_field(name="Kraliçeniz geldi.", value=f"Önünde diz çökün {message.author.mention}.`Hoş geldin!`", inline=False)
                
                await message.channel.send(embed=embed)
                await message.add_reaction(emoji)



def setup(bot):
    bot.add_cog(spamverbs())