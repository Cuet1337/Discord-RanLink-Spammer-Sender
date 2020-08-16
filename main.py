import random
import discord 
import time 
import asyncio
from discord.ext import commands

prefix = '#'

token = 'TOKEN-HERE'

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f'Ready, use {prefix}send or {prefix}spammer to spam/send links!')

def getlinkFromFile():
  with open("links.txt", 'r') as linkFile:
    contents = linkFile.read().split("\n")
    return contents[random.randint(0, len(contents))]

@bot.command()
async def send(ctx):
    await ctx.message.delete()
    await ctx.send(f'{getlinkFromFile()}')

@bot.command()
async def spammer(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send(f'{getlinkFromFile()}')

bot.run(token, bot=False)
