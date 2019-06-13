import discord
from classes.rps import spelen 
from classes.samson import quote
from classes.burger import burger_moment
from discord import Game
from discord.ext import commands
import random




bot = commands.Bot(command_prefix='!')

client = discord.Client()

@bot.event
async def on_ready():
    arr = ['broodt eten','zwemmen in de water', 'grt zeggen', 'kwaken', 'eent zijn', 'playing playing playing playing', 'xD', 'owo', 'uwu', 'asbest eten', 'asbest verwijderen', 'waggelen']

    print (bot.user.name)
    await bot.change_presence(activity=discord.Game(name=random.choice(arr)))

@bot.command()
async def rps(ctx, *args):
    await ctx.send(spelen(args))


@bot.command()
async def quoteS(ctx, *args):
    await ctx.send(quote(args))


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if 'grt' in message.content:
        await message.channel.send('grt')






 




bot.run('NTg1Nzk5NjQzNzgzNDk1Njgy.XPkMig.aZepKp_bHwFXnaTjIo7tBFFuNnw')