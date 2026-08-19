import os

import discord
from discord.ext import commands
from modals.modal import *
from dropdowns.dropdown import *
from buttons.button import *

client = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name='hello')
async def hello(interaction: discord.Interaction, member : discord.Member=None):
    if member is None:
        await interaction.response.send_message(f'Hello {interaction.user.mention}')

    else:
        await interaction.response.send_message(f'Hello {member.mention}')

@client.tree.command(name='modal')
async def modal(interaction: discord.Interaction):
    await interaction.response.send_modal(MyModal())

@client.tree.command(name="button")
async def button(interaction: discord.Interaction):
    await interaction.response.send_message("Here's the button", view=MyButton(), ephemeral=True)

@client.tree.command(name="dropdown")
async def dropdown(interaction: discord.Interaction):
    await interaction.response.send_message("Pick your favourite colour:", view=DropdownView(), ephemeral=True)




token = "TOKEN"  # Replace with your actual bot token or use environment variable

client.run(token)