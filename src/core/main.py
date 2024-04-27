import disnake
from disnake.ext import commands
import utils

config = utils.general.load_configuration()

class MyBot(commands.Bot):
    def __init__(self):
        self.config = config
        self.utils = utils
    
    super().__init__(test_guilds=config['test_guilds'])