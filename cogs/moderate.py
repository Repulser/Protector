from discord.ext.commands import Cog
import ml


class Moderate(Cog):
    """
    Automatic moderation
    """

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        print(ml.predict(message.content))
