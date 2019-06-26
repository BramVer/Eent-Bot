import discord
from classes.rps import spelen 
from classes.samson import quote
from classes.burger import burger_moment
from classes.weertje import huidig_weer
from classes.vang_maar import vangen

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

@bot.command()
async def weertje(ctx):
    await ctx.send(huidig_weer())
    await ctx.send(file=discord.File('classes/weerbericht.jpg'))



@bot.command()
async def vang(ctx):
    await ctx.send(vangen())   
    await ctx.send(file=discord.File('classes/pokemon.jpg')) 

@bot.command()
async def eent(ctx):
    await ctx.send(eent())
    await ctx.send(file=discord.File('classes/eent.jpg'))


@bot.event
async def on_message(message):
    arrGeluk = ['Je bent van de trap gevallen en hebt nu hersenschade', 'Je bent op een stuk lego gaan staan, sterkte!', 'idk ge zijt gwn dood lol xd']
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if 'grt' in message.content:
        await message.channel.send('```grt```')
    if 'burger' in message.content:
        await message.channel.send(burger_moment())
        await message.channel.send(file=discord.File('classes/borger.png'))
    if 'ongeluk' in message.content:
        await message.channel.send(random.choice(arrGeluk))
    if 'lole' in message.content:
        await message.channel.send('xd')
    if 'weertje' in message.content:
        await message.add_reaction('🏓')
    if 'voeten' in message.content:
        await message.channel.send(file=discord.File('classes/sniff.png'))






 




bot.run('geheim dit mag je niet stelen')
