"""
Declare variables used in bot.
This file is a based on the variables.py file from my other bot.
"""
import json
import os
from logging.handlers import RotatingFileHandler

import discord

# v[major].[minor].[release].[build]
# MAJOR and MINOR version changes can be compatibility-breaking
VERSION = "v0.0.0.2"
PROG_DIR = os.path.dirname(os.path.realpath(__file__))
API_URL = "https://api-inference.huggingface.co/models/Hobospider132/DialoGPT-Mahiru-Proto"
MODEL_NAME = "Hobospider132/DialoGPT-Mahiru-Proto"
intents = discord.Intents.default()
handler = RotatingFileHandler(
    filename=os.path.join(PROG_DIR, "log", "discord.log"),
    encoding="utf-8",
    mode="w",
    backupCount=10,
    maxBytes=100000,
)
# pylint: disable=line-too-long
error_quotes = ["I'm sorry, I don't seem to be understanding your request. Perhaps I need to hit the books a bit harder!",
                "I'm trying my best to help you, but it seems like I need to study a little more. Can you please provide me with more information?",
                "Oh dear, it seems like my knowledge is limited in this area. Let me know how I can better assist you!",
                "I'm still learning and growing, just like a diligent student. Can you please try your request again or provide more context?",
                "I'm sorry, it looks like I'm missing some crucial information. Could you please rephrase your request or provide more details?",
                "I'm sorry, I don't seem to be getting the hang of things just yet. Could you please try your request again or give me more details?",
                "I'm doing my best to assist you, but it seems like I'm having some trouble. Can you please help me understand what you need?",
                "It looks like I need a little more practice to get this right. Can you please try your request again?",
                "I'm still learning the ropes, so please bear with me. Can you please try rephrasing your request or giving me more information?"
                ]
# pylint: enable=line-too-long


class Secret:
    """Class for secret.json management"""

    def __init__(self) -> None:
        self._file = os.path.join(PROG_DIR, "secret.json")
        with open(self._file, encoding="utf-8", mode="r") as secret_f:
            self.secrets = json.load(secret_f)
        self.token = self.secrets["token"]
        self.htoken = self.secrets.get("htoken", False)

    def __repr__(self) -> str:
        return "[OBFUSCATED]"

    def __str__(self) -> str:
        return "[OBFUSCATED]"
