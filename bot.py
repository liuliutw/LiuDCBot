import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True  # 啟用成員事件

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(1307355346469130293)  # 替換為正確的頻道 ID
    if channel:
        await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(1307355346469130293)  # 替換為正確的頻道 ID
    if channel:
        await channel.send(f'{member} leave!')

bot.run(TOKEN)
