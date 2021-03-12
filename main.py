import discord
import json
import os
import datetime
import random
import pyfiglet
import asyncio
import time

from discord.ext import commands, tasks
from discord import Embed
from discord import Message
from discord.utils import get


with open("./data/config.json", "r") as configfile:
    configdata = json.load(configfile)
    token = configdata["discord_token"]
    prefix = configdata["prefix"]

epoch = datetime.datetime.utcfromtimestamp(0)
time_diff = round((datetime.datetime.utcnow() - epoch).total_seconds())

os.chdir(r'C:\Users\taha6\Desktop\CQBot')

intents = discord.Intents(messages=True, guilds=True, members=True, presences=True)

class Center(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix=prefix, pm_help=None, Description="CenterQuickBot Türkçe Discord Bot!", intents=intents)

    async def on_ready(self):
        await bot.change_presence(activity=discord.Game(name="?yardım   CenterQuickBot "))
        cqb = pyfiglet.figlet_format("CenterQuickBot", font="slant")
        print(cqb)
        #t = time.gmtime(time.time())
        #self.ui.log(f"Bot başarıyla giriş yaptı {t.tm_hour}:{t.tm_min}")
        print("Bot Adı : ", self.user.name)
        print("Bot İD : ", self.user.id)
        print("-" * 50)

    async def on_member_join(self, member):
        
        print(f"Sunucuya {member} Katıldı...")

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == "sa":
            if message.author.id == 721798616200773722:
                return

            if message.author.id == 795338483270942740:
                return

            if message.author.id == 717317491604324383:
                return

            if message.author.id == 465464440452677638:
                return
            
            if message.author.id == 785868634341113876:
                return

            else:
                emoji = "👋"
                await message.channel.send(f"{message.author.mention} **Aleyküm Selam** Hoş Geldin.")
                await message.add_reaction(emoji)

        if message.content == "Sa":
            if message.author.id == 721798616200773722:
                return

            if message.author.id == 795338483270942740:
                return

            if message.author.id == 717317491604324383:
                return

            if message.author.id == 465464440452677638:
                return
            
            if message.author.id == 785868634341113876:
                return

            else:
                emoji = "👋"
                await message.channel.send(f"{message.author.mention} **Aleyküm Selam** Hoş Geldin.")
                await message.add_reaction(emoji)
 
        if message.content == "bot":
            emoji = "👀"
            await message.channel.send("**Buradayım**")
            await message.add_reaction(emoji)

        if message.content == "naber":
            await message.channel.send("**İyi Senden Naber**")

        if message.content == "Naber":
            await message.channel.send("**İyi Senden Naber**")

        if message.content == "neden":
            await message.channel.send("***KAPLUMBAĞA DEDEN***")

        if message.content == "<@!784141794153332786>":
            emoji = "👀"
            await message.channel.send("İşlem devam ediyor...")
            await asyncio.sleep(3)
            await message.channel.send("Prefix : ?")

        #if message.content == "tag":
        #    await message.channel.send("¹³")

        if message.content == "yardım":
            embed = discord.Embed(title='CenterQuickBot Help.', description="", color = 0xfffcfc)
            embed.add_field(name="Üye komutları", value = "`avatar` | `profil` | `sunucu`\n`yaz` | `yazdır`", inline=False)
            embed.add_field(name="Moderation Module", value="`kick` | `ban` | `dm`\n`duyuru` | `temizle` | `yavaşla`\n`mute` | `unmute` | `uyar`", inline=False)
            embed.add_field(name="Oyunlar", value="`duello` | `tahmin` | `sor`\n`çevir` | `yazıtura`\n`dilek`", inline=False)
            embed.add_field(name="Eğlence komutları", value="`sarıl` | `tokat` | `dans`\n`öp` | `aşk` | `kedi`\n`köpek` | `kahve`", inline=False)
            embed.add_field(name="Bot", value="`botbilgi` | `davet`", inline=False)
            embed.add_field(name="**Prefix**", value="**?**")
            embed.add_field(name="Botu Yapan", value="<@721798616200773722>")
    
            await message.channel.send(embed=embed)

        await self.process_commands(message) ##

        #self.ui.log(f"{message.author.name} : {message.content}")


bot = Center()
bot.load_extension("komutlar.fun")
bot.load_extension("komutlar.member")
bot.load_extension("komutlar.moderator")
bot.load_extension("komutlar.number")
bot.load_extension("komutlar.info")
bot.load_extension("komutlar.level")
bot.load_extension("komutlar.level_add_role")
bot.load_extension("komutlar.slots")
bot.load_extension("komutlar.para")
bot.load_extension("komutlar.message")
bot.load_extension("komutlar.8ball")
bot.load_extension("komutlar.rulet")
bot.load_extension("komutlar.spam")
bot.load_extension("komutlar.voice")
bot.load_extension("komutlar.luck")
bot.load_extension("komutlar.economy")
bot.load_extension("komutlar.warn")
bot.run(token)
