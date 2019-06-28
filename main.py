from discord.ext import commands
import utils

description = ''

bot = commands.Bot(command_prefix='-', description=description)


@bot.event
async def on_ready():
    print("Ready!")


bot.load_extension("cogs.moderate")

if __name__ == '__main__':
    config = utils.load_config()
    if config:
        bot.run(config['token'])
