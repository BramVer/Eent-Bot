

import discord
from classes.rps import spelen 
from classes.burger import burger_moment
from discord import Game
from discord.ext import commands




bot = commands.Bot(command_prefix='!')

client = discord.Client()

@bot.event
async def on_ready():
    arr = ['broodt eten','zwemmen in de water', 'grt zeggen', 'kwaken', 'eent zijn', 'playing playing playing playing', 'xD', 'owo', 'uwu']

    print (bot.user.name)
    await bot.change_presence(activity=discord.Game(name='broodt eten'))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'grt' in message.content:
        await message.channel.send('grt')

@bot.command()
async def test(ctx, *args):
    await ctx.send(' '.join(args))

@bot.command()
async def rps(ctx, *args):
    await ctx.send(spelen(args))


 




bot.run('NTg1Nzk5NjQzNzgzNDk1Njgy.XPkMig.aZepKp_bHwFXnaTjIo7tBFFuNnw')