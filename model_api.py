"""This file is used to access the model either locally or via the HuggingFace API."""
from typing import Tuple
import os
import logging

import aiohttp
try:
    from transformers import Conversation, pipeline
    LOCAL = True
except ImportError:
    LOCAL = False

from variables import MODEL_NAME, API_URL, Secret


class Mahiru:
    """Class for accessing Mahiru AI."""
    def __init__(self):
        self._secret = Secret()
        self._client = None
        self._pipeline = None
        force_online = int(os.environ.get("FORCE_ONLINE", 0))
        if LOCAL and not force_online:
            logging.info("Using local model")
            self._pipeline = pipeline("conversational",
                                      model=MODEL_NAME,
                                      use_auth_token=self._secret.htoken,)
            return
        if self._secret.htoken:
            logging.info("Using API model")
            self._session = aiohttp.ClientSession()
            return
        raise ValueError("No valid model access method found")

    async def talk(self, data: str) -> Tuple[int, str]:
        """Talk with the Mahiru AI model."""
        if self._pipeline:
            conversation = Conversation(data)
            self._pipeline(conversation)
            return (0,conversation.generated_responses[-1])

        payload = {"inputs": {"text": data}}
        header = { "Authorization": f"Bearer {self._secret.htoken}" }
        async with self._session.post(API_URL, json=payload, headers=header, timeout=60) as resp:
            result = await resp.json()
            if result.get("error", None):
                if result["error"] == f"Model {MODEL_NAME} is currently loading":
                    return (2, "Model is currently loading")
                return (1, result["error"])
            return (0, result["generated_text"])
