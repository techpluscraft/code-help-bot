import os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("Bot is ready!")
    
# for loop that loads all the commands
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')
        
client.run(os.getenv('TOKEN'))