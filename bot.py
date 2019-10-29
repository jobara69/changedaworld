import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print ('Bot is ready')

client.run('NjM4NDkzMTY0NTIwNDcyNTg3.Xbh7eA.tjLf1ZXOWvVsQZAH2Co8UtIeBZ8')
