from discord.ext import commands
from discord.ext.commands import Cog
import ml
import utils


class Moderate(Cog):
    """
    Automatic moderation
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.name == self.bot.config['log_channel']:
            return
        prediction = await ml.predict(message.content)  # Get prediction from API
        print(f'{message.content} - {prediction}')
        classification = prediction[0]
        score = prediction[1]
        if classification == 'notok':
            if score > 0.8:  # Delete if score is good
                await message.delete()
            await self.handle_message(message, score)

    async def handle_message(self, message, score):
        channel = [c for c in message.guild.text_channels if c.name == self.bot.config['log_channel']]
        if channel:
            channel = channel[0]
            if score > 0.8:
                await channel.send(
                    f"\N{LARGE RED CIRCLE} `[{utils.get_time_string()}]` {message.channel.mention} **Harmful message by** `{message.author.name}#{message.author.discriminator} ({message.author.id})` **was deleted:** `{utils.clean_message(message.content)}`"
                )
            else:
                await channel.send(
                    f"\N{LARGE ORANGE DIAMOND} `[{utils.get_time_string()}]` {message.channel.mention} **Potentially harmful message by** `{message.author.name}#{message.author.discriminator} ({message.author.id})` **Content:** `{utils.clean_message(message.content)}`"
                )


def setup(bot):
    bot.add_cog(Moderate(bot))
