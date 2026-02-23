import discord
from discord.ext import commands
import os
import asyncio

TOKEN = os.getenv("MTQ1ODg1MTk3NTY1ODYwMjQ5Ng.GZUNSI._l45rBTrkGb_qKnkN2j6xNwtYNpcBqqxCcNsy4")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    reconnect=True
)

<@&1459023594448224288>.event
async def on_ready():
    print(f"✅ Bot online sebagai {bot.user}")
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game("Online 24 Jam 🚀")
    )

<@&1459023594448224288>.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 {round(bot.latency * 1000)}ms")

# Auto reconnect loop
async def start_bot(MTQ1ODg1MTk3NTY1ODYwMjQ5Ng.GZUNSI._l45rBTrkGb_qKnkN2j6xNwtYNpcBqqxCcNsy4):
    while True:
        try:
            await bot.start(TOKEN)
        except Exception as e:
            print(f"Bot crash: {e}")
            await asyncio.sleep(5)

asyncio.run(start_bot())
