import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith("!"):
        await message.delete()
        await message.channel.send(message.content)

    await bot.process_commands(message)

bot.run("TOKEN")
