import asyncio
import datetime
import discord
import time
import math
from discord.ext import commands

TOKEN = 'Memes are cool'

bot = commands.Bot(command_prefix="+",
                   description='A bot who watches streams!')

bot.starttime = datetime.datetime.now()
bot.startup_done = False

initial_extensions = ['announce']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(f"cogs.{extension}")

@bot.event
async def on_ready():
    print("I'm ready for announcements!")
    await bot.change_presence(activity=discord.Activity(name='The streams', type=discord.ActivityType.watching))

bot.run(TOKEN)