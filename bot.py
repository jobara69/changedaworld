import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Finalmente vivo'))
    print ('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')
    
client.run(os.environ['DISCORD_TOKEN'])
