import nextcord, datetime
from nextcord.ext import commands

class starboard(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, member):
        schannel = self.client.get_channel(944370019075239997)
        if (reaction.emoji == '⭐') and (reaction.count >= 1):
            embed = nextcord.Embed(color = nextcord.Color.fuchsia())
            embed.set_author(name = reaction.message.author.name, icon_url = reaction.message.author.avatar.url)
            embed.add_field(name = "Message Content", value = f"{reaction.message.content} [Jump]({reaction.message.jump_url})")
            
            if len(reaction.message.attachments) > 0:
                embed.set_image(url = reaction.message.attachments[0].url)
            embed.set_footer(text = f" ⭐ {reaction.count} | # {reaction.message.channel.name}")
            embed.timestamp = datetime.datetime.utcnow()
            await schannel.send(embed = embed)
            
def setup(client):
    client.add_cog(starboard(client))