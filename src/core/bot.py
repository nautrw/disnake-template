import os
import platform
import sys
from typing import List

import disnake
from disnake.ext import commands
from loguru import logger

import src.utils as utils

# Load the bot's documentation from the configuration file.
config = utils.general.load_configuration("src/core/config.json")


class Bot(commands.InteractionBot):
    """
    A subclass of commands.InteractionBot that represents the main bot instance.
    Methods:
        load_extensions: Loads the extensions specified in the configuration file.
        main: Starts the bot.
    """

    def __init__(self) -> None:
        """
        Initializes the bot's class with configuration and utilities, and sets up basic settings.
        """
        self.config: dict = config
        self.utils = utils

        super().__init__(test_guilds=config["test_guilds"])

    def load_extensions(self, exts_list: List[str]) -> None:
        """
        Loads the extensions specified in the configuration file. Logs to the console after loading each extension.

        Args:
            exts_list (List[str]): A list of extensions to load.
        """
        loaded_exts_count = 0
        for ext in exts_list:
            try:
                self.load_extension(ext)
                logger.debug(f"Loaded extension {ext}")
                loaded_exts_count += 1
            except Exception as exception:
                exception = f"{type(exception).__name__}: {exception}"
                logger.error(f"Failed to load extension {ext}:\n{exception}")

        logger.success(
            f'{loaded_exts_count} extension{"s" if loaded_exts_count != 1 else ""} loaded'
        )

    async def on_connect(self) -> None:
        """
        Event handler for when the bot connects to Discord. Logs various information about the bot.
        """
        logger.info(f"Connected to {len(self.guilds)} guilds")
        logger.info(f"Using Disnake version {disnake.__version__}")
        logger.info(f"Using Python version {sys.version}")
        logger.info(
            f"Using platform {platform.system()} {platform.release()} {os.name}"
        )
        logger.success(f"Successfully logged in as {self.user} (ID: {self.user.id})")

    def main(self) -> None:
        """
        Main function for the bot that starts it.
        """
        self.load_extensions(self.config["exts"])
        self.run(config["token"])
