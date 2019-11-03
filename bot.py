import discord
from discord.ext import commands
import os
from discord.utils import get
import random
import youtube_dl
from os import system

client = commands.Bot(command_prefix = '.')
olavo_imagens = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnxnEMfxft1FdkQZ00Uco7xgjrky0zDkSOZJnLtsNAx7WeCx7MqQ&s','https://static.congressoemfoco.uol.com.br/2018/11/olavo-de-carvalho.png','https://static.poder360.com.br/2019/03/Olavo-de-Carvalho-868x644.png']

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
async def play(ctx, url: str):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove ('song.mp3')
            print ('Removed old song file')
    except PermissionError:
        print ('Trying to delete song file, but its being played')
        await ctx.send ('ERROR: Ta tocando música')
        return

    await ctx.send ('Ta quase tocando, retardado')
    
    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print ('Downloading audio now\n')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print ('Renamed File: {file}\n')
            os.rename(file, 'song.mp3')

    voice.play (discord.FFmpegPCMAudio ('song.mp3'), after = lambda e: print (f'{name} has finished playing'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
    
    nname = name.rspit('-', 2)
    await ctx.send (f'Playing: {nname}')
    print ('playing\n')
    
@client.command()
async def olavo(ctx):
    embed = discord.Embed (color=0xff69b4)
    embed.set_image (url = 'https://i.imgur.com/QsRNR5N.jpg')
    embed.set_footer(text=f'Olavo não está feliz')

    await ctx.send(embed=embed)

@client.command()
async def triste(ctx):
    embed = discord.Embed (color=0xff69b4)
    embed.set_image (url = 'https://acegif.com/wp-content/gifs/sad-cat-60-gap.jpg')
    embed.set_footer (text=f'to triste')
    await ctx.send(embed=embed)

@client.command()
async def honk(ctx):
    embed = discord.Embed (color=0xff69b4)
    embed.set_image (url = 'https://i.kym-cdn.com/photos/images/newsfeed/001/566/686/65f.jpg')
    embed.set_footer (text=f'Honk honk')
    await ctx.send(embed=embed)

@client.command()
async def suicidio(ctx):
    embed = discord.Embed (color=0xff69b4)
    embed.set_image (url = 'https://i.kym-cdn.com/photos/images/original/001/581/013/142.gif')
    embed.set_footer (text=f'Vou ali e já volto')
    await ctx.send(embed=embed)

@client.command()
async def olavo2(ctx):
    chosen_image = random.choice (olavo_imagens)
    embed = discord.Embed (color=0xff69b4)
    embed.set_image (url = chosen_image)
    await ctx.send (embed=embed)

client.run(os.environ['DISCORD_TOKEN'])
