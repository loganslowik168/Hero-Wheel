import discord
from discord.ext import commands

from secrets import BOT_TOKEN as TOKEN

# Set up the bot with the command prefix
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author == bot.user:
        return

    # Check if the message is "marco" (case insensitive)
    if message.content.lower() == "marco":
        await message.channel.send("polo")

    # Ensure other commands are still processed
    await bot.process_commands(message)

# Replace "YOUR_TOKEN_HERE" with your bot's token
bot.run(TOKEN)
