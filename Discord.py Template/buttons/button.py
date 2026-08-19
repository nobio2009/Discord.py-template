import discord

class MyButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Green', style=discord.ButtonStyle.green)
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is green.', ephemeral=True)

#@client.tree.command(name="buttonmenu")
#async def menu(interaction: discord.Interaction):
#    await interaction.response.send_message("Here's the button", view=MyButton())