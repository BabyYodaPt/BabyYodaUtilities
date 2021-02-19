import discord
from discord.ext import commands 
import asyncio
import random


from PIL import Image,ImageFont,ImageDraw
from io import BytesIO
from random import randint

client = commands.Bot(command_prefix = "b/")

@client.command()
async def verdade(ctx):
  lista = ['verdadeiro✅', 'mentira❌']
  resp = random.choice(lista)
  await ctx.reply(f'O que voce disse é **' + resp + '**')

@client.command()
async def moeda(ctx):
    list = ['Cara', 'Coroa']
    res = random.choice(list)
    await ctx.channel.send('A moeda girou e o resultado foi **' + res + '**')

@client.command()
async def ping(ctx):
    await ctx.message.add_reaction('🏓')
    await ctx.reply(f'🏓Pong! A Lantecia da API é **{round(client.latency * 1000)}ms**')


@client.command()
async def gay(ctx):
    mention = {ctx.author.metion}
    numero_random = randint(1, 100)
    embed = discord.Embed(
    title="🏳️‍🌈Gay Test",
    description='🌈 ' + mention + ' é **{}%** gay'.format(numero_random),
    colour=discord.Colour(0x008EFF),
    )
    embed.set_image(
    url="https://i.imgur.com/uHGTsON.gif"
    )
    await ctx.reply(
    embed=embed,
)

@client.command()
async def faustão(ctx, *, text = "No text enterd"):

    img = Image.open("./img/faustaotemp.jpg")
    
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 60)
    
    draw.text((200,0), text, (0,0,0), font=font)
    
    img.save("faustão.jpg")

    await ctx.send(file = discord.File("faustão.jpg"))
    
@client.command()
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    
    wanted = Image.open("./img/wantedtemp.jpg")

    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((177,177))

    wanted.paste(pfp, (120,212))

    wanted.save("wanted.jpg")

    await ctx.send(file = discord.File("wanted.jpg"))

    
    
client.run('token')