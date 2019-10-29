import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print ('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send('Pong! {round(client.latency * 1000)} ms')
    
client.run(os.environ['DISCORD_TOKEN'])
