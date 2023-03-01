"""The main cog. Contains 'mainstream' utilities."""
import logging
import json
import requests

import discord
from discord import app_commands
from discord.ext import commands

from variables import API_URL, Secret

scrt = Secret()

def query(payload):
    """ Make a request to the Hugging Face model API """
    data = json.dumps(payload)
    response = requests.request('POST',
                                API_URL,
                                headers={ "Authorization": f"Bearer {scrt.htoken}" },
                                data=data,
                                timeout=60)

    ret = json.loads(response.content.decode('utf-8'))
    return ret

class Utility(commands.Cog, name="Main Utilities"):
    """Main bot utilities"""

    def __init__(self, bot: commands.Bot):
        self._bt = bot
        logging.info("Loaded %s", self.__class__.__name__)

    @app_commands.command(
        name="mahiru", description="Speak with Mahiru AI!"
    )
    async def mahiru(self, ctx: discord.Interaction, content: str):
        """Speak with Mahiru AI!"""
        await ctx.response.defer()
        payload = {"inputs": {"text": content}}
        response = query(payload)
        bot_response = response.get("generated_text", None)

        if not bot_response:
            if 'error' in response:
                bot_response = f"Error: {response['error']}"
            else:
                bot_response = "Hmm... something is not right."

        # send the model's response to the Discord channel
        await ctx.followup.send(bot_response)

async def setup(bot: commands.Bot):
    """Setup function for the cog."""
    await bot.add_cog(Utility(bot))
