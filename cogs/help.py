from matplotlib.style import available
import nextcord
from nextcord.ext import commands, tasks
import datetime

AVAILABLE = 943261823153602561
OCCUPIED = 943262546742362142
DORMANT = 943262612639059999

HELP = [943264593516560435,943264659383926837,943264818322899034]

class help(commands.Cog, name="Help"):
    def __init__(self,client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if not message.author.bot:
            if message.channel.id in HELP:
                if not message.content.lower() == "!close":
                    occupiedcat = await self.client.fetch(OCCUPIED)
                    channel = message.channel
                    await channel.edit(category=occupiedcat)
    
    @tasks.loop(minutes=10)
    async def dormantcheck(self):
        for channel in HELP:
            channel = await self.client.fetch_channel(channel.id)
            if channel.category_id == DORMANT:
                last_message = self.client.fetch_message(channel.last_message_id)
                if nextcord.utils.utcnow() - last_message.created_at > datetime.timedelta(minutes=30):
                    availablecat = await self.client.fetch(AVAILABLE)
                    await channel.edit(category=availablecat)
                    
    @commands.command()
    async def close(self,ctx):
        dormantcat = await self.client.fetch(DORMANT)
        channel = ctx.channel
        embed = nextcord.Embed(title="Help Closed",description="The help channel has been closed.",color=nextcord.Colors.red)
        await ctx.send(embed=embed)
        await channel.edit(category=dormantcat)

def setup(client):
    client.add_cog(help(client))