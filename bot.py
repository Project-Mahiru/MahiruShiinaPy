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
    logging.info("Bot version: %s", VERSION)
    logging.info("Discord.py version: %s", discord.__version__)
    await bot.change_presence(status=discord.Status.idle,
                            activity=discord.Activity(type=discord.ActivityType.playing,
                                                       name="with Chitose")
                            )
    await bot.load_extension("main_utils")
    await bot.tree.sync()
    logging.info("Finished loading cogs.")
    print("Tech's Note: This is weird but the repo owner wants it so sure.\n\n"
          f"Project [Mahiru] {VERSION} startup complete.\n"
          f"Discord.py version: {discord.__version__}\n"
          f"Bot user: {bot.user}\n\n"
          "Disclaimer:\n"
          "This bot is not affiliated with the author of Otonari no Tenshi-sama in any way.\n"
          "The AI model does not represent the author's views in any way.\n"
          "Please do not use this bot to harass the author or anyone else.")

if __name__ == "__main__":
    if os.environ.get("LIVE_DEBUG"):
        bot.run(scrt.token, log_level=logging.INFO, log_handler=logging.StreamHandler())
    elif os.environ.get("DEBUG"):
        bot.run(scrt.token, log_level=logging.INFO, log_handler=handler)
    else:
        bot.run(scrt.token, log_level=logging.WARN, log_handler=handler)
