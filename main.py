from bot_init import *
from secret_config import TOKEN

import mahitka_commands.help_group
import mahitka_commands.events

import mahitka_commands.role_commands.leaders
import mahitka_commands.role_commands.level
import mahitka_commands.role_commands.role
import mahitka_commands.role_commands.setlevel
import mahitka_commands.role_commands.setpoint
import mahitka_commands.role_commands.role_reset
import context_menus.level_context_menu
import context_menus.sex_context_menu

@bot.listen()
async def on_ready():
    await bot.tree.sync()

    
bot.run(TOKEN)