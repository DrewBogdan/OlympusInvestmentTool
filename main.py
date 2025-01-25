import discord
import asyncio
from discord import Client
from discord.ext.commands import Bot
from discord.ext import commands
from colorama import Fore, Back, Style

from DiscordBot.Hermes import Hermes
from DiscordBot.cogs import stock_cog

async def setup(bot):
    await bot.add_cog(stock_cog.Stocks(bot))

if __name__ == '__main__':

    print(Back.BLACK + Fore.CYAN + "[PROGRAM] bot starting up..." + Style.RESET_ALL)

    token = open('DiscordBot/token.txt').read()

    intents=discord.Intents(messages=True, message_content=True, guilds=True, reactions=True)

    bot = Hermes(command_prefix='$', intents=intents)

    asyncio.run(setup(bot))

    bot.run(token)
