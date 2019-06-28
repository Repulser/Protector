from discord.ext import commands
import utils

description = ''

bot = commands.Bot(command_prefix='-', description=description)

if __name__ == '__main__':
    config = utils.load_config()
    if config:
        bot.run(config['token'])

