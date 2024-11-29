import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.event
async def on_member_join(member):
    print(f'{member}join!')
    #channel = bot.get_channel(1312070988665716817)
    #await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')
    #channel = bot.get_channel(1312071051475292201)
    #await channel.send(f'{member}leave!')

bot.run('MTMwNzM1NDQ5MjM5NTg0Nzc3Mg.GRSML8.yE4pyIDSvBx4NAQVkXW4IDeTH9x_MSywQOlajs')