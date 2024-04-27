import disnake
from disnake.ext import commands
from loguru import logger
import src.utils as utils
import os

config = utils.general.load_configuration()


class Bot(commands.InteractionBot):
    def __init__(self):
        self.config = config
        self.utils = utils

        super().__init__(test_guilds=config["test_guilds"])

    def load_extensions(self, exts_list: list):
        loaded_exts_count = 0
        for ext in exts_list:
            try:
                self.load_extension(ext)
                logger.info(f"Loaded extension {ext}")
                loaded_exts_count += 1
            except Exception as exception:
                exception = f"{type(exception).__name__}: {exception}"
                logger.error(f"Failed to load extension {ext}:\n{exception}")
        
        logger.info(f'{loaded_exts_count} extensions loaded')

    def main(self):
        self.load_extensions(self.config['exts'])
        self.run(config["token"])