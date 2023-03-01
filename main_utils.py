"""The main cog. Contains 'mainstream' utilities."""
import logging

from discord import app_commands
from discord.ext import commands

import json
import requests

def query(self, payload):
""" make request to the Hugging Face model API """

data = json.dumps(payload)
response = requests.request('POST',
   'https://api-inference.huggingface.co/models/Hobospider132/DialoGPT-Mahiru-Proto',
    headers={ 'Authorization': 'Bearer Hoob\'s API' },
    data=data)

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
    async def ping(self, ctx):
        payload = {'inputs': {'text': ctx.content}}
        response = self.query(payload)
        bot_response = response.get('generated_text', None)

        if not bot_response:
            if 'error' in response:
                bot_response = '`Error: {}`'.format(response['error'])
            else:
                bot_response = 'Hmm... something is not right.'

        # send the model's response to the Discord channel
        await ctx.channel.send(bot_response)

async def setup(bot: commands.Bot):
    """Setup function for the cog."""
    await bot.add_cog(Utility(bot))
