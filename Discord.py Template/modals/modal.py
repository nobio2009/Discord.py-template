import discord

class MyModal(discord.ui.Modal, title='Example Modal with All Input Types'):
    # A short text input (default), great for names, small fields, etc.
    short_text = discord.ui.TextInput(
        label='Short Text (default)',                  # The label shown to the user
        placeholder='Enter some short text',           # Placeholder text before user types
        required=True                                  # Make this field mandatory
    )

    # A paragraph-style input for longer responses
    paragraph_text = discord.ui.TextInput(
        label='Paragraph Text',
        style=discord.TextStyle.paragraph,             # Makes it a multiline textbox
        placeholder='Write a longer message here...',
        required=False                                 # Optional input
    )

    # A numeric input using min_length and max_length (not strictly validated as number, but useful hint)
    number_like_text = discord.ui.TextInput(
        label='Number-Like Input',
        placeholder='Enter a number (1-999)',
        min_length=1,                                  # Require at least 1 character
        max_length=3                                   # Limit to 3 characters
    )

    async def on_submit(self, interaction: discord.Interaction):
        # Build a response showing all inputs (except hidden if you want to leave that out)
        await interaction.response.send_message(
            f"Short: {self.short_text.value}\n"
            f"Paragraph: {self.paragraph_text.value}\n"
            f"Number-Like: {self.number_like_text.value}",
            ephemeral=True
        )
