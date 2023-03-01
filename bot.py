"""The main bot file. Start the bot."""
import logging
import os

import discord
from discord.ext import commands

from variables import VERSION, Secret, intents, handler

bot = commands.Bot(command_prefix="~", intents=intents)
scrt = Secret()


@bot.event
async def on_ready():
    """Logs bot readiness"""
    logging.info("Connected to Discord as %s", bot.user)
    logging.info("Project [Mahiru] version: %s", VERSION)
    logging.info("Discord.py version: %s", discord.__version__)
    await bot.change_presence(status=discord.Status.idle,
                            activity=discord.Activity(type=discord.ActivityType.playing,
                                                       name="with Chitose")
                            )
    await bot.load_extension("main_utils")
    await bot.tree.sync()
    logging.info("Finished loading cogs.")

if __name__ == "__main__":
    if os.environ.get("LIVE_DEBUG"):
        hndlr = logging.StreamHandler()
        bot.run(scrt.token, log_level=logging.INFO, log_handler=hndlr, root_logger=True)
    elif os.environ.get("DEBUG"):
        bot.run(scrt.token, log_level=logging.INFO, log_handler=handler, root_logger=True)
    else:
        bot.run(scrt.token, log_level=logging.WARNING, log_handler=handler, root_logger=True)
