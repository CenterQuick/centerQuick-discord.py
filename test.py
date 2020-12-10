        with open('users.json', 'r') as f:
            users = json.load(f)

        await ctx.update_data(users, message.author)
        await ctx.add_experience(users, message.author, 1)
        await ctx.level_up(users, message.author, message.channel)

        with open('users.json', 'w') as f:
            json.dump(users, f)
        await bot.process_commands(message)

    async def update_data(self, users, user):
        if not user.id in users:
            users[user.id] = {}
            users[user.id]['experience'] = 0
            users[user.id]['level'] = 0

    async def add_experience(self, users, user, exp):
        users[user.id]['experience'] += exp

    async def level_up(self, ctx, users, user, channel):
        experience = users[user.id]['experience']
        lvl_start = user[user.id]['level']
        lvl_end = int(experience ** (1/4))

        if lvl_start < lvl_end:
            await ctx.send.channel("{} Seviye atladın :lvl_up:! Şu anda ki seviyen {} ".format(user.mention, lvl_end))
            users[user.id]['level'] = lvl_end