import discord
from discord.ext import commands 
import asyncio
import random


from PIL import Image
from io import BytesIO
from random import randint

client = commands.Bot(command_prefix = "b/")

@client.command()
async def verdade(ctx):
  lista = ['verdadeiro', 'mentira']
  resp = random.choice(lista)
  await ctx.reply(f'O que voce disse é ' + resp)

@client.command()
async def moeda(ctx):
  list = ['cara', 'coroa']
  res = random.choice(list)
  await ctx.channel.send('A moeda girou e o resultado foi ' + res)

@client.command()
async def ping(ctx):
    await ctx.reply(f'🏓Pong! A Lantecia da API é{round(client.latency * 1000)}ms')

@client.command()
async def gay(ctx):
    ctx.send("comando em reforma")


@client.command()
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    
    wanted = Image.open("wantedtemp.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((177,177))

    wanted.paste(pfp, (120,212))

    wanted.save("wanted.jpg")

    await ctx.send(file = discord.File("wanted.jpg"))

    

client.run('Nzg5NDk0MTM0NjU4MTcwODgx.X9y3tQ.IhIoGXwPSBuH3Cj2mdcjz0YVlW8')
