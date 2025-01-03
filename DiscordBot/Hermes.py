# class for discord bot Hermes
import discord
from discord import Client
from discord.ext.commands import Bot
import Log as l


class Hermes(Bot):
    def __init__(self, command_prefix, **options):
        self.LOG = l.Log("[HERMES]", "yellow")
        self.LOG.print("Initiating Hermes...")
        super().__init__(command_prefix, **options)

