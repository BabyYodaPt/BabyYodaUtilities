import discord
from discord.ext import commands 
import asyncio
import random

from PIL import Image
from io import BytesIO

client = commands.Bot(command_prefix = "b/")


@client.command()
async def ping(ctx):
    await ctx.reply('Pong!')

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

    wanted.save("profile.jpg")

    await ctx.send(file = discord.File("wanted.jpg"))

    

client.run('token')
