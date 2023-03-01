"""The main cog. Contains 'mainstream' utilities."""
import logging

from discord import app_commands
from discord.ext import commands

class Utility(commands.Cog, name="Main Utilities"):
    """Main bot utilities"""

    def __init__(self, bot: commands.Bot):
        self._bt = bot
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

async def setup(bot: commands.Bot):
    """Setup function for the cog."""
    await bot.add_cog(Utility(bot))
