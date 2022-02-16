import nextcord
from nextcord.ext import commands, tasks
import aiohttp
from urllib import parse

class googleit(commands.Cog, name="Google it"):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name='googleit',
        aliases=['lmgt', 'letme'],
    )
    async def googleit(self, ctx, string: str):
        """Return a url link that animate a google research."""
        stringed_array = " ".join(word[:50] for word in string.split(' ')[:32])  # Maximum of 32 words, and a word has 50 chars max.
        query = parse.quote_plus(stringed_array)

        await ctx.send("The google tool is very powerful, see how it works!")
        await ctx.send(f"https://letmegooglethat.com/?q={query}")

def setup(client):
    client.add_cog(googleit(client))