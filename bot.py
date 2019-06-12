

import discord
from classes.rps import spelen 
from discord import Game
from discord.ext import commands



bot = commands.Bot(command_prefix='$')

client = discord.Client()

@bot.event
async def on_ready():
    print (bot.user.name)
    await bot.change_presence(activity=discord.Game(name='broodt eten'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.command()
async def test(ctx, *args):
    await ctx.send(' '.join(args))

@bot.command()
async def rps(ctx, *args):
    await ctx.send(spelen(args))
 




bot.run('NTg1Nzk5NjQzNzgzNDk1Njgy.XPkMig.aZepKp_bHwFXnaTjIo7tBFFuNnw')