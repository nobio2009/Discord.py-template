import discord

class MyModal(discord.ui.Modal, title='MyModal'):
    text_1 = discord.ui.TextInput(label='Text-1: ')
    text_2 = discord.ui.TextInput(label='Text-2: ')

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Modal submitted', ephemeral=True)