import discord
import asyncio
from discord import Client
from discord.ext.commands import Bot
from discord.ext import commands

from DiscordBot.Hermes import Hermes
from DiscordBot.cogs import util_cog

async def setup(bot):
    await bot.add_cog(util_cog.Util(bot))

if __name__ == '__main__':
    token = open('DiscordBot/token.txt').read()

    intents=discord.Intents(messages=True, message_content=True, guilds=True, reactions=True)

    bot = Hermes(command_prefix='$', intents=intents)

    asyncio.run(setup(bot))

    print("[HERMES] bot starting up...")

    bot.run(token)
