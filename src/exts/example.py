import disnake
from disnake.ext import commands


class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction) -> None:
        """
        Returns the bot's ping.
        """
        await inter.response.send_message(f"Pong! `{round(self.bot.latency * 1000)}`ms")

def setup(bot):
    bot.add_cog(Example(bot))
