"""The main cog. Contains 'mainstream' utilities."""
import asyncio
import logging
import re

import discord
from discord import app_commands
from discord.ext import commands

from variables import VERSION

class Utility(commands.Cog, name="Main Utilities"):
    """Main bot utilities"""

 def __init__(self, model_name):
        # adding intents module to prevent intents error in __init__ method in newer versions of Discord.py
        intents = discord.Intents.default() # Select all the intents in your bot settings as it's easier
        intents.message_content = True
        super().__init__(intents=intents)
        self.api_endpoint = API_URL + model_name
        # retrieve the secret API token from the system environment
        huggingface_token = os.environ['HUGGINGFACE_TOKEN']
        # format the header in our request to Hugging Face
        self.request_headers = {
            'Authorization': 'Bearer {}'.format(huggingface_token)
        }
        logging.info("Loaded %s", self.__class__.__name__)

    @app_commands.command(
        name="ping", description="The classic ping command. Checks the bot's latency."
    )
    async def ping(self, ctx):
        """This command is used to check if the bot is online."""
        await ctx.response.send_message(
            "Pong! The bot is online.\nPing: "
            + str(round(self._bt.latency * 1000))
            + "ms"
        )
        await self._bt.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing, name="with tickets!"
            )
        )


