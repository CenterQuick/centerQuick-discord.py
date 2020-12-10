import discord
import json
import os
import datetime

from discord.ext import commands, tasks

with open("./data/config.json", "r") as configfile:
    configdata = json.load(configfile)
    token = configdata["discord_token"]

default_prefix = "?"

epoch = datetime.datetime.utcfromtimestamp(0)
time_diff = round((datetime.datetime.utcnow() - epoch).total_seconds())

os.chdir(r'C:\Users\taha6\Desktop\CQBot')


intents = discord.Intents(messages=True, guilds=True, members=True, presences=True)

class CQB(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix=default_prefix, pm_help=None, Description="CenterQuickBot Türkçe Discord Bot!", intents=intents)

    async def on_ready(self):
        print("CenterQuickBot **Hazır!**")
        print(self.user.name)
        print(self.user.id)
        print("-----------------")

    async def on_member_join(self, ctx, member):
        with open('./data/users.json', 'r') as f:
            users = json.load(f)

        await ctx.update_data(users, member)

        with open('./data/users.json', 'w') as f:
            json.dump(users, f)


    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == "sa":
            await message.channel.send("**Aleyküm Selam HoşGeldin!**")

        if message.content == "Sa":
            await message.channel.send("**Aleyküm Selam HoşGeldin!**")

        if message.content == "bot":
            await message.channel.send("**Buradayım**")

        await self.process_commands(message) ##



bot = CQB()
bot.load_extension("komutlar.fun")
bot.load_extension("komutlar.member")
bot.load_extension("komutlar.moderator")
bot.load_extension("komutlar.number")
bot.load_extension("komutlar.info")
bot.load_extension("komutlar.level")
bot.load_extension("komutlar.level_add_role")
bot.load_extension("komutlar.slots")
bot.load_extension("komutlar.para")
bot.run(token)