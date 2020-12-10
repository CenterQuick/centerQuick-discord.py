import random
import discord

from discord.ext import commands

sayı = ('0','1','2','3','4','5','6','7','8','9')

class randomnumber(commands.Cog):
    @commands.command(name="tahmin")
    async def number(self, ctx, message):
        number = random.randint(0, 9)
        for i in range(0, 5):
            await ctx.send('Tekrar')
            response = await ctx.bot.wait_for('message')
            guess = int(response.content)
            if guess > number:
                await ctx.send('Büyük tahmin')
            elif guess < number:
                await ctx.send('Küçük tahmin')
            else:
                await ctx.send('**Tebrikler Bildin!!!**')



def setup(bot):
    bot.add_cog(randomnumber())