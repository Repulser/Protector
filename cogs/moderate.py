from discord.ext.commands import Cog
import ml


class Moderate(Cog):
    """
    Automatic moderation
    """

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        prediction = await ml.predict(message.content)
        if prediction[0] is 'notok':
            if prediction[1] > 0.8:
                await message.delete


def setup(bot):
    bot.add_cog(Moderate(bot))
