import disnake
from disnake.ext import commands
from loguru import logger

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def reload_extension(self, inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
        """
        Reloads an extension.
        """
        try:
            self.bot.reload_extension(extension)
            await inter.response.send_message(f"Reloaded extension {extension}")
            logger.debug(f"Reloaded extension {extension}")
        except Exception as exception:
            exception = f"{type(exception).__name__}: {exception}"
            await inter.response.send_message(exception)
            
    @commands.slash_command()
    async def unload_extension(self, inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
        """
        Unloads an extension.
        """
        try:
            self.bot.unload_extension(extension)
            await inter.response.send_message(f"Unloaded extension {extension}")
            logger.debug(f"Unloaded extension {extension}")
        except Exception as exception:
            exception = f"{type(exception).__name__}: {exception}"
            await inter.response.send_message(exception)
    
    @commands.slash_command()
    async def load_extension(self, inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
        """
        Loads an extension.
        """
        try:
            self.bot.load_extension(extension)
            await inter.response.send_message(f"Loaded extension {extension}")
            logger.debug(f"Loaded extension {extension}")
        except Exception as exception:
            exception = f"{type(exception).__name__}: {exception}"
            await inter.response.send_message(exception)

def setup(bot):
    bot.add_cog(Developer(bot))
