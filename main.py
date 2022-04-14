import os
from nextcord.ext import commands
from dotenv import load_dotenv
from cogs.buttons.sr_view import SRView

load_dotenv()

client = commands.Bot(command_prefix='!')
client.persistent_views_added = False

@client.event
async def on_ready():
    print("Bot is ready!")
    client.load_extension("commands.buttons.sr_message")
    if not client.persistent_views_added:
        client.add_view(SRView())
    client.persistent_views_added = True
    print('loading persistent views')
    
# for loop that loads all the commands
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        
client.run(os.getenv("TOKEN"))