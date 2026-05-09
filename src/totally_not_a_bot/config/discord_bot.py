import discord


class TotallyNotABot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())


# TODO investigate intents for discord.py
# TODO discord bot to have heartbeats
