import discord
import youtube_dl
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game ('me mata, por favor'))
    print ('Bot is ready')

@client.command(aliases = ['J', 'joi'])
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

client.run('NjM4NDkzMTY0NTIwNDcyNTg3.Xbewtw.hC4IID02hwMWeyhKTOtztNeyN0g')
