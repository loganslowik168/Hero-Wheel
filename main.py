import discord
from discord.ext import commands
import random

from scripts import GetOptions
from secrets import BOT_TOKEN as TOKEN
import heroes

# Set up the bot with the command prefix
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

spin_help_message = ("Usage: `!spin [game] [optional category]`\n"
                     "**Available games:** rivals, overwatch\n"
                     "**Available categories:** dps/dmg/damage/duelist, tank/vanguard, support/healer/heal/strategist"
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    # Prevent the bot from responding to itself
    if message.author == bot.user:
        return

    '''
    # Check if the message is "marco" (case insensitive)
    if message.content.lower() == "marco":
        await message.channel.send("polo")
    '''
    # Ensure other commands are still processed
    await bot.process_commands(message)

@bot.command()
async def spin(ctx, game: str = None, category: str = None):
    """
    Spins to randomly select an character from a predefined list based on the selected game.
    
    Usage: !spin [game] [optional category]
    """
    # Determine the list to use
    ops = GetOptions(game.lower() if game else None, category.lower() if category else None)

    # If bad inputs
    if isinstance(ops, ValueError):
        await ctx.message.reply(spin_help_message)
        return
    # The list must be good

    await ctx.message.reply(f"Selected hero: {random.choice(ops)}")
bot.run(TOKEN)
