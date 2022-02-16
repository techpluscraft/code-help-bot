from nextcord.ext import commands

AUTO_THREAD_CHANNEL = 943613618426109962

class autothread(commands.Cog,name="Auto Thread"):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id == AUTO_THREAD_CHANNEL:
            await message.create_thread(name="Discussion")


def setup(client):
    client.add_cog(autothread(client))