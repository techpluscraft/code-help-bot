import nextcord

VIEW_NAME = "SRView"
HELPERS_ID = "943260696735535215"
ALERTS_ID = "964276690303979590"
POLLS_ID = "964276657001226270"

class SRView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def handle_click(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        role_id=int(button.custom_id.split(":")[-1])
        role = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)
        
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Your {role.name} role has been removed.", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"You have been given the {role.name} role.", ephemeral=True)

    def custom_id(view: str, id: int) -> str:
        return f"{view}:{id}"
    
    @nextcord.ui.button(label="Helpers (NOT STAFF)", style=nextcord.ButtonStyle.primary, custom_id='SRView:943260696735535215', emoji="✋")
    async def HELPERS_button(self, button, interaction):
        await self.handle_click(button, interaction)
    
    @nextcord.ui.button(label="Announcements Ping", style=nextcord.ButtonStyle.primary, custom_id='SRView:964276690303979590', emoji="📣")
    async def ALERTS_button(self, button, interaction):
        await self.handle_click(button, interaction)
    
    @nextcord.ui.button(label="Poll Pings", style=nextcord.ButtonStyle.primary, custom_id='SRView:964276657001226270', emoji="💡")
    async def PP_button(self, button, interaction):
        await self.handle_click(button, interaction)