import discord
from discord.ext import commands, tasks
import os
from discord.utils import get
import random

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
        print (f'O bot foi conectado no {channel}\n')

    responses = [f'Ui, que delícia, entrei no {channel}',
                f'Kebab time no {channel}',
                f'Separa a vó do carlos pra mim no {channel}',
                f'Fudeu, tem uma bomba no {channel}',
                f'Mulher é merda, só no {channel}']

    await ctx.send(f'{random.choice(responses)}')

@client.command ()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'Desconectado do {channel}')

        responses = [f'Saí dessa merda que é o {channel}',
                    f'Só tem vagabundo, prostituta e drogado no {channel}',
                    f'Tenho que levar minha vó no jiu-jitsu',
                    f'O {channel} é gay',
                    f'Carlos chupa pica no {channel}']
        
        await ctx.send (f'{random.choice(responses)}')
    else:
        print ('Não tem como desconectar, não ta em sala nenhuma')

        responses = ['Porra, tu ta querendo demais',
                     'O bot não ta em sala nenhuma, mongoloide',
                     'vai se fuder, deixa o bot em paz',
                     'vô comer tua mãe',
                     'calos leite de minhápica',
                     'vai se fuder, porra, quer que o bot saia sem nem ta em lugar nenhum']

        await ctx.send (f'{random.choice(responses)}')

@client.command()
async def olavo(ctx):
    embed = discord.Embed (color=0xff69b4, timestamp=datetime.datetime.utcnow())
    embed.set_image (url = 'https://i.imgur.com/QsRNR5N.jpg')
    embed.set_footer(text=f'Olavo não está feliz')

    await ctx.send(embed=embed)

client.run(os.environ['DISCORD_TOKEN'])
