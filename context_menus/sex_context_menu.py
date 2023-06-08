import discord
from discord.ext import commands
from discord import app_commands
from bot_init import bot
from bot_init import basa

async def levelContextMenu(interaction: discord.Interaction, message: discord.Message):


    if not message.content.startswith("https://tenor.com"):
        await interaction.response.send_message(
            "Это не гифка tenor",
            ephemeral=True
        )
        return
    
    if message.author.id == interaction.user.id: await message.delete()
    
    await interaction.response.send_message("https://txnor.com" + message.content.replace("https://tenor.com", ""))


sex_context_menu = app_commands.ContextMenu(
    name="sex",
    callback=levelContextMenu
)

bot.tree.add_command(sex_context_menu)