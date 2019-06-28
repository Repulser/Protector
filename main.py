import asyncio

import discord
from discord.ext import commands
import utils

description = ''

bot = commands.Bot(command_prefix='-', description=description)
bot.remove_command("help")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f'{bot.command_prefix}help'),
                              status=discord.Status.online)
    print("Ready!")


@bot.command(name="help")
async def get_help(ctx):
    await ctx.send(
        "\N{INFORMATION SOURCE} **For information about Protector and how to use it please check out our GitHub page at: https://github.com/Repulser/Protector**")


bot.load_extension("cogs.moderate")

if __name__ == '__main__':
    config = utils.load_config()
    if config:
        bot.config = config
        bot.run(config['token'])
