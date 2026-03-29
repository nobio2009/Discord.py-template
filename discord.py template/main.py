import discord
from discord.ext import commands
from discord import app_commands
import sys

from modals.modal import *
from dropdowns.dropdown import *
from buttons.button import *

# ---- TOKEN FROM CMD ARG ----
if len(sys.argv) < 2:
    print("Usage: python main.py <TOKEN>")
    sys.exit(1)

TOKEN = sys.argv[1]

# ----------------------------

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    client.add_view(PersistentView())

    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@client.tree.command(name='hello')
async def hello(interaction: discord.Interaction, member: discord.Member = None):
    if member is None:
        await interaction.response.send_message(f'Hello {interaction.user.mention}')
    else:
        await interaction.response.send_message(f'Hello {member.mention}')

@client.tree.command(name='modal')
async def modal(interaction: discord.Interaction):
    await interaction.response.send_modal(MyModal())

@client.tree.command(name='button')
async def button(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Here's the button:",
        view=PersistentView()
    )

@client.tree.command(name='dropdown')
async def dropdown(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Pick your favourite colour:",
        view=DropdownView()
    )

# ---- RUN BOT ----
client.run(TOKEN)