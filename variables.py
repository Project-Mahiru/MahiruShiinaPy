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
VERSION = "v0.0.0.1"
PROG_DIR = os.path.dirname(os.path.realpath(__file__))

intents = discord.Intents.default()
handler = RotatingFileHandler(
    filename=os.path.join(PROG_DIR, "log", "discord.log"),
    encoding="utf-8",
    mode="w",
    backupCount=10,
    maxBytes=100000,
)


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
