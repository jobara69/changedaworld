import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print ('Bot is ready')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        await message.channel.send('Bando de gay')
        
client.run(os.environ['DISCORD_TOKEN'])
