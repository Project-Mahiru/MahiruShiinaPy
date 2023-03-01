"""The main bot file. Start the bot."""
import logging

import discord
from discord.ext import commands

from variables import VERSION, Secret, intents

bot = commands.Bot(command_prefix="~", intents=intents)
scrt = Secret()


@bot.event
async def on_ready():
    """Logs bot readiness"""
    print("Connected to Discord as %s", bot.user)
    print("Bot version: %s", VERSION)
    print("Discord.py version: %s", discord.__version__)
    bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with Chitose"))
    await bot.load_extension("main_utils")
    await bot.tree.sync()
    logging.info("Finished loading cogs.")


if __name__ == "__main__":
    bot.run(scrt.token)
