import random
import discord

from discord.ext import commands
from discord import message


class pvp(commands.Cog):
    @commands.command(name="düello")
    async def düello(self, ctx, message):
        if len(ctx.message.mentions) != 1:
            await ctx.send(f"Lütfen bu şekilde kullanınız: `?düello @isim`")
        else:
            oyuncu2 = ctx.message.mentions[0]
            oyuncu1 = ctx.message.author
            can1 = 500
            can2 = 500
            saldırı = random.randint(0, 250)
            can3 = 0
            can4 = 0

            await ctx.send("**Düello Başlıyor**")
            for d in range(0, 3):
                if message.content == 'saldır':
                    await ctx.send(f"{oyuncu2.name} canı", can2 - saldırı == can3, "azaldı.")
                    await ctx.send(f"Sıradaki {oyuncu2.name} ")

                elif message.content == 'saldır':
                    await ctx.send(f"{oyuncu1.name} canı", can1 - saldırı == can4, "azaldı.")
                    await ctx.send(f"Sıradaki {oyuncu1.name} ")

            if can3>can4:
                await ctx.send(f"{oyuncu2.name} Kazandı. **Tebrikler**")

            elif can3<can4:
                await ctx.send(f"{oyuncu1.name} Kazandı. **Tebrikler**")

            elif can3 == can4:
                await ctx.send("**Berabere**")


def setup(bot):
    bot.add_cog(pvp())