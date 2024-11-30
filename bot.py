import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True  # 啟用成員事件

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(1312070988665716817)  # 替換為正確的頻道 ID
    if channel:
        await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(1312071051475292201)  # 替換為正確的頻道 ID
    if channel:
        await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

