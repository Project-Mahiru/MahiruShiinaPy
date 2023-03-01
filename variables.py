"""
Declare variables used in bot.
This file is a based on the variables.py file from my other bot.
"""
import json
import os


import discord

# v[major].[minor].[release].[build]
# MAJOR and MINOR version changes can be compatibility-breaking
VERSION = "v0.0.2.5"
PROG_DIR = os.path.dirname(os.path.realpath(__file__))

intents = discord.Intents.default()
intents.message_content = True  # pylint: disable=assigning-non-slot


class Secret:
    """Class for secret.json management"""

    def __init__(self) -> None:
        self._file = os.path.join(PROG_DIR, "secret.json")
        with open(self._file, encoding="utf-8", mode="r") as secret_f:
            self.secrets = json.load(secret_f)
        self.token = self.secrets["token"]

    def __repr__(self) -> str:
        return "[OBFUSCATED]"

    def __str__(self) -> str:
        return "[OBFUSCATED]"


