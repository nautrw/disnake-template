import disnake
from disnake.ext import commands
from loguru import logger
import utils

config = utils.general.load_configuration()


class Bot(commands.Bot):
    def __init__(self):
        self.config = config
        self.utils = utils

    super().__init__(test_guilds=config["test_guilds"])

    def load_extensions(self, exts_dir: str):
        loaded_exts_count = 0
        for ext in os.listdir(exts_dir):
            extname = ext[:-3]
            try:
                self.load_extension(f"{exts_dir}.{extname}")
                logger.info(f"Loaded extension {extname}")
                loaded_exts_count += 1
            except Exception as exception:
                exception = f"{type(exception).__name__}: {exception}"
                logger.error(f"Failed to load extension {extname}:\n{exception}")

    def main(self):
        self.load_extensions("src.exts")
        self.run(config["token"])
