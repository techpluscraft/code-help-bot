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
        self.dormantcheck.start()
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if not message.author == self.client.user:
            if message.channel.id in HELP:
                if not message.content.lower() == "!close":
                    occupiedcat = await self.client.fetch_channel(OCCUPIED)
                    channel = message.channel
                    pins = await channel.pins()
                    pins = [pin.id for pin in pins]
                    if len(pins) < 2:
                        guild = message.guild
                        await channel.edit(category=occupiedcat)
                        await message.pin()
                        author = message.author
    
    @tasks.loop(minutes=10)
    async def dormantcheck(self):
        for channel in HELP:
            channel = await self.client.fetch_channel(channel)
            if channel.category_id == DORMANT:
                last_message = await channel.history(limit=1).flatten()
                if nextcord.utils.utcnow() - last_message[0].created_at > datetime.timedelta(minutes=30):
                    availablecat = await self.client.fetch_channel(AVAILABLE)
                    await channel.edit(category=availablecat)
                    await channel.send("This channel has been dormant for over 30 minutes. It has been moved to the available category.")
                    
    @dormantcheck.before_loop
    async def beforedormantcheck(self):
        await self.client.wait_until_ready()
        print("Dormant check is starting")
                    
    @commands.command(name="close",description="Close the help channel.")
    async def close(self,ctx):
        """"Close the help channel."""
        dormantcat = await self.client.fetch_channel(DORMANT)
        channel = ctx.channel
        embed = nextcord.Embed(title="Help Closed",description="The help channel has been closed.")
        await ctx.send(embed=embed)
        await channel.edit(category=dormantcat)
        pins = await channel.pins()
        pins = [str(pin.id) for pin in pins]
        if channel.id == 943264818322899034:
            pins.remove("943317744273735710")
        if channel.id == 943264659383926837:
            pins.remove("943317688334295040")
        if channel.id == 943264593516560435:
            pins.remove("943317564480712734")
        
        pins = "".join(pins)
        pins = int(pins)
        rem_pin = await channel.fetch_message(pins)
        rem_author = rem_pin.author
        rem_auth = await self.client.fetch_user(rem_author.id)
        guild = ctx.guild
        await rem_pin.unpin()

def setup(client):
    client.add_cog(help(client))
