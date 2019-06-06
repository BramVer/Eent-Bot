# Work with Python 3.6
import discord
from classes.rand import RandomGetal

TOKEN = "NTg1Nzk5NjQzNzgzNDk1Njgy.XPkMig.aZepKp_bHwFXnaTjIo7tBFFuNnw"

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention} !!!!!'.format(message)
        await client.send_message(message.channel, msg)
    if 'moeke' in message.content:
        msg = 'oooh moeke'.format(message)
        await client.send_message(message.channel,msg)

    if message.content.startswith('!rtd'):
        msg = RandomGetal().format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)