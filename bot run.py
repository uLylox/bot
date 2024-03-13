# IMPORTS

import discord
from discord.ext import commands
import os
import random as r
import requests


# COMMANDS


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} logged in.')

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hellow! I'm a bot designed by Lylox and still improving. My main functions are being a chatbot and command bot!")

@bot.command()
async def heh(ctx, count_heh = 5):
    if count_heh < 1000:
        await ctx.send("he" * count_heh)
    else:
        await ctx.send("Discord doesn't let me send over 2000 letters! Therefore the maximum input is 999 :(")
        

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined in {discord.utils.format_dt(member.joined_at)}, Nice stats buddy! :)')

@bot.command()
async def bye(ctx):
    await ctx.send(f"Bye!!")

@bot.command()
async def animecat(ctx):
    pictures = os.listdir("Pictures")
    picture = r.choice(pictures)
    with open(f"Pictures/{picture}", 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


def catDef():
    url = 'https://api.thecatapi.com/v1/images/search'
    res = requests.get(url)
    data = res.json()
    print(data)
    print(data[0])
    return data[0]["url"]

def duckDef():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    print(data)
    return data["url"]

def dogDef():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    print(data)
    return data["url"]

def foxDef():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    print(data)
    return data["url"]

def pokemonDef():
    url = 'https://pokeapi.co'
    res = requests.get(url)
    data = res.json()
    print(data)
    return data["url"]




@bot.command()
async def cat(ctx):
    image_url = catDef()
    await ctx.send(image_url)


@bot.command()
async def duck(ctx):
    image_url = duckDef()
    await ctx.send(image_url)


@bot.command()
async def dog(ctx):
    image_url = dogDef()
    await ctx.send(image_url)


@bot.command()
async def fox(ctx):
    image_url = foxDef()
    await ctx.send(image_url)


@bot.command()
async def pokemon(ctx):
    image_url = pokemonDef()
    await ctx.send(image_url)


@bot.command()
async def Saving(ctx):
    await ctx.send(f"Saving Energy and Water: They can reduce the amount of waste by saving energy and water at home. For example, they can reduce energy consumption by using LED lamps or have taps repaired.")



@bot.command()
async def Reusing(ctx):
    await ctx.send(f"Reusing Projects: They can reuse unused items in their home and use them for new purposes or start recycling projects by using their manual skills.")



@bot.command()
async def Recycling(ctx):
    await ctx.send(f"Recycling: They can recycle used items by putting them in a recycling trash can, leading to it being reused by others in the future without any more raw material usage.")



@bot.command()
async def SpreadingAwareness(ctx):
    await ctx.send(f"Spreading Awareness: They can spread awareness and give information to other people like their family, leading to a waste reduction.")



@bot.command()
async def WhereToPutTrash(ctx):
    await ctx.send("""Where To Put Trash In The Recycle Bins: 
                                    
GLASS RECYCLE BIN:
Glass cups, glass bottles, literally any piece of glass and etc.

METAL RECYCLE BIN:
Used soda/cola/drink cans, electronic waste, iron pieces, kitchen stuff, building waste and etc.

PAPER RECYCLE BIN:
Used books, notebooks, cardboard and etc.

PLASTIC RECYCLE BIN:
Plastic bottles, plastic toys, plastic glass and etc.

ORGANIC RECYCLE BIN:
Organic food, fruits, vegetables. Apples, carrots, oranges, bananas and etc.""")
    




# BOT RUN


bot.run("token")
