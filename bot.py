"""The main bot file. Start the bot."""
import logging
import os

import discord
from discord.ext import commands

from variables import VERSION, Secret, intents, handler


class Mahiru(commands.Bot):
    """Class for the bot itself."""

    async def setup_hook(self):
        """Setup for the bot."""
        logging.info("Project [Mahiru] version: %s", VERSION)
        logging.info("Discord.py version: %s", discord.__version__)
        await self.load_extension("main_utils")
        return await super().setup_hook()


bot = Mahiru(
    command_prefix=commands.when_mentioned,
    intents=intents,
    status=discord.Status.idle,
    activity=discord.Activity(type=discord.ActivityType.playing, name="with Chitose"),
)
scrt = Secret()


if __name__ == "__main__":
    if os.environ.get("LIVE_DEBUG"):
        hndlr = logging.StreamHandler()
        bot.run(scrt.token, log_level=logging.INFO, log_handler=hndlr, root_logger=True)
    elif os.environ.get("DEBUG"):
        bot.run(
            scrt.token, log_level=logging.INFO, log_handler=handler, root_logger=True
        )
    else:
        bot.run(
            scrt.token, log_level=logging.WARNING, log_handler=handler, root_logger=True
        )
