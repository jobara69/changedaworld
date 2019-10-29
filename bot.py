import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print ('Bot is ready')

client.run('NjM4NDkzMTY0NTIwNDcyNTg3.Xbh7eA.tjLf1ZXOWvVsQZAH2Co8UtIeBZ8')
