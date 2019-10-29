import discord
from discord.ext import commands, tasks
import os
from discord.utils import get

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game('Finalmente vivo'))
    print ('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

@client.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print (f'The bot has connected to {channel}\n')

    await ctx.send(f'Entrei gostoso no {channel}')

@client.command ()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'Desconectado do {channel}')
        await ctx.send (f'O bot foi dar o cu e deixou o {channel}')
    else:
        print ('Acho que meu pai é gay')
        await ctx.send ('vai se fuder, porra, quer que o bot saia sem nem ta em lugar nenhum')

client.run(os.environ['DISCORD_TOKEN'])
