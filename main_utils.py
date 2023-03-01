"""The main cog. Contains 'mainstream' utilities."""
import logging
from random import choice

import asyncio
import discord
from discord import app_commands
from discord.ext import commands

from variables import error_quotes
from model_api import Mahiru

class Utility(commands.Cog, name="Main Utilities"):
    """Main bot utilities"""

    def __init__(self, bot: commands.Bot):
        self._bt = bot
        self._mahiru = Mahiru()
        logging.info("Loaded %s", self.__class__.__name__)

    @app_commands.command(
        name="mahiru", description="Speak with Mahiru AI!"
    )
    async def mahiru(self, ctx: discord.Interaction, content: str):
        """Speak with Mahiru AI!"""
        await ctx.response.defer()
        exit_code, response = await self._mahiru.talk(content)
        if exit_code == 1:
            message = choice(error_quotes) + \
                "\nI'm sorry, it seems like there's been a miscommunication." +\
                f" Please try again or ask for help if needed.\n\nError: {response}"
            logging.error("Model failed to respond with errror: %s",message)
            await ctx.followup.send(message, ephemeral=True)
            return
        if exit_code == 2:
            await asyncio.sleep(60)
            exit_code, response = await self._mahiru.talk(content)
            if exit_code == 1:
                message = "**Mahiru**: " + choice(error_quotes) + \
                    "\nI'm sorry, it seems like there's been a miscommunication." +\
                    f" Please try again or ask for help if needed.\n\nError: {response}"
                logging.error("Model failed to respond with errror: %s",message)
                await ctx.followup.send(message, ephemeral=True)
                return
            if exit_code == 2:
                message = "**DEVELOPER**: Oh dear, it seems like Mahiru isn't ready to talk yet." +\
                    " Please try again later and if the issue persist contact staff."
                logging.warning("Model failed to wake up after 60 seconds.")
                await ctx.followup.send(message, ephemeral=True)
                return
        convo = f"**{ctx.user.name}**: {content}\n**Mahiru**: {response}"
        await ctx.followup.send(convo)

async def setup(bot: commands.Bot):
    """Setup function for the cog."""
    await bot.add_cog(Utility(bot))
