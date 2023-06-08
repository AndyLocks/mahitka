import discord
from bot_init import basa
from variables.constant import *
from discord.ext import commands
from random import randint
from variables.constant import RARE_IMAGE, IMAGES, EMBED_COLOR, BLACK_LIST_CHANNELS

async def user_role_management(message: discord.Message):

    if message.channel.id in BLACK_LIST_CHANNELS: return
    if message.guild == None: return
    if message.guild.id == SERVERID and await basa.chek(message.author.id):
        level = await basa.get_point(message.author.id)
        await basa.set_point(memberId=message.author.id, value=level+1)
        level += 1

        if level % 100 == 0 and level != 0:
            level = level // 100
            emb = discord.Embed(
                                description=f"Поздравляю с {level} уровнем! <:leopardik:1061619000481689600>",
                                color=EMBED_COLOR
                                )
            
            if randint(0, 1000) == 1:
                emb.set_image(url=RARE_IMAGE)
            
            else:
                emb.set_image(url=IMAGES[randint(0, len(IMAGES)-1)])

            await message.guild.get_channel(NOTIFICATIONS_CHANNEL).send(f"<@{message.author.id}>", embed=emb)
        
            await management_role(ctx=message)


async def management_role(ctx: commands.context.Context | discord.Message, user: discord.Member = None):
    if ctx.guild == None: return
    if ctx.guild.id == SERVERID and await basa.chek(ctx.author.id):
        point = await basa.get_point(memberId=ctx.author.id)
        level = point // 100

        for i in range(len(LEVELS)):
            if level == 0:
                role_index = 0
                break
            if level in range(int(LEVELS[i+1])):
                role_index = i
                break
        
        choise = await basa.get_choise(memberId=ctx.author.id)

        member: discord.Member = user if user else ctx.author
        
        if choise == "Bounty-Hunter":
            author_roles_id = []
            for i in member.roles:
                author_roles_id.append(i.id)

            range_roles = set(BOUNTYHUNTERS_ROLES)

            roles = set(author_roles_id) & range_roles

            for i in roles:
                if i == BOUNTYHUNTER: continue

                role = ctx.guild.get_role(i)
                await member.remove_roles(role)
            role_id = BOUNTYHUNTERS_ROLES[role_index]
                
            await member.add_roles(ctx.guild.get_role(role_id))

        elif choise == "Pirate":
            author_roles_id = []
            for i in member.roles:
                author_roles_id.append(i.id)

            range_roles = set(PIRATES_ROLES)

            roles = set(author_roles_id) & range_roles

            for i in roles:
                if i == PIRATE: continue

                role = ctx.guild.get_role(i)
                await member.remove_roles(role)
            role_id = PIRATES_ROLES[role_index]
                
            await member.add_roles(ctx.guild.get_role(role_id))

        elif choise == "Marine":
            author_roles_id = []
            for i in member.roles:
                author_roles_id.append(i.id)

            range_roles = set(MARINES_ROLES)

            roles = set(author_roles_id) & range_roles

            for i in roles:
                if i == MARINE: continue
                role = ctx.guild.get_role(i)
                await member.remove_roles(role)

            role_id = MARINES_ROLES[role_index]

            await member.add_roles(ctx.guild.get_role(role_id))