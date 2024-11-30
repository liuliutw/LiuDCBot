import discord
from discord.ext import commands
import json
import random

with open('setting.json',mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
intents.members = True  # 啟用成員事件

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(int(jdata['welcome']))  # 替換為正確的頻道 ID
    if channel:
        await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(int(jdata['leave']))  # 替換為正確的頻道 ID
    if channel:
        await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

@bot.command()
async def 你是哪一派(ctx):
    radomImage=random.choice(jdata['image1'])
    image=discord.File(radomImage)
    await ctx.send(file=image)

bot.run(jdata['TOKEN'])