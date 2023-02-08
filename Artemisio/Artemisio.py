import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 1067562113826029709:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        if payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name="Valorant")
        elif payload.emoji.name == '🤓':
            role = discord.utils.get(guild.roles, name="LoL")
        elif payload.emoji.name == '🔫':
            role = discord.utils.get(guild.roles, name="CS")
        elif payload.emoji.name == '⛵':
            role = discord.utils.get(guild.roles, name="Sea of Thieves")
        elif payload.emoji.name == '😒':
            role = discord.utils.get(guild.roles, name="Overwatch")
        elif payload.emoji.name == '⛏️':
            role = discord.utils.get(guild.roles, name="Minecraft")
        else:
            return
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        await member.remove_roles(role)
    elif message_id == 1067577052758294598:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        if payload.emoji.name == '🦉':
            role = discord.utils.get(guild.roles, name="Amigos Ruben")
        elif payload.emoji.name == '🦦':
            role = discord.utils.get(guild.roles, name="Amigos Goncalo")
        elif payload.emoji.name == '🐆':
            role = discord.utils.get(guild.roles, name="Amigos Lucas")
        elif payload.emoji.name == '🦝':
            role = discord.utils.get(guild.roles, name="Amigos Ze")
        elif payload.emoji.name == '🐂':
            role = discord.utils.get(guild.roles, name="Amigos Renato")
        elif payload.emoji.name == '🐒':
            role = discord.utils.get(guild.roles, name="Amigos Samuel")
        elif payload.emoji.name == '🐗':
            role = discord.utils.get(guild.roles, name="Amigos Alentejano")
        elif payload.emoji.name == '🦍':
            role = discord.utils.get(guild.roles, name="Amigos Pedro")
        elif payload.emoji.name == '🐐':
            role = discord.utils.get(guild.roles, name="Amigos Miguel")
        elif payload.emoji.name == '🐴':
            role = discord.utils.get(guild.roles, name="Amigos Cabeludo")
        elif payload.emoji.name == '🐣':
            role = discord.utils.get(guild.roles, name="Amigos Careca")
        elif payload.emoji.name == '🐰':
            role = discord.utils.get(guild.roles, name="Amigos Beatriz")
        elif payload.emoji.name == '🦋':
            role = discord.utils.get(guild.roles, name="Amigos Barbara")
        else:
            return
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        await member.remove_roles(role)

@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1067562113826029709:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        if payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name="Valorant")
        elif payload.emoji.name == '🤓':
            role = discord.utils.get(guild.roles, name="LoL")
        elif payload.emoji.name == '🔫':
            role = discord.utils.get(guild.roles, name="CS")
        elif payload.emoji.name == '⛵':
            role = discord.utils.get(guild.roles, name="Sea of Thieves")
        elif payload.emoji.name == '😒':
            role = discord.utils.get(guild.roles, name="Overwatch")
        elif payload.emoji.name == '⛏️':
            role = discord.utils.get(guild.roles, name="Minecraft")
        else:
            return
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        await member.add_roles(role)
    elif message_id == 1067577052758294598:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)
        if payload.emoji.name == '🦉':
            role = discord.utils.get(guild.roles, name="Amigos Ruben")
        elif payload.emoji.name == '🦦':
            role = discord.utils.get(guild.roles, name="Amigos Goncalo")
        elif payload.emoji.name == '🐆':
            role = discord.utils.get(guild.roles, name="Amigos Lucas")
        elif payload.emoji.name == '🦝':
            role = discord.utils.get(guild.roles, name="Amigos Ze")
        elif payload.emoji.name == '🐂':
            role = discord.utils.get(guild.roles, name="Amigos Renato")
        elif payload.emoji.name == '🐒':
            role = discord.utils.get(guild.roles, name="Amigos Samuel")
        elif payload.emoji.name == '🐗':
            role = discord.utils.get(guild.roles, name="Amigos Alentejano")
        elif payload.emoji.name == '🦍':
            role = discord.utils.get(guild.roles, name="Amigos Pedro")
        elif payload.emoji.name == '🐐':
            role = discord.utils.get(guild.roles, name="Amigos Miguel")
        elif payload.emoji.name == '🐴':
            role = discord.utils.get(guild.roles, name="Amigos Cabeludo")
        elif payload.emoji.name == '🐣':
            role = discord.utils.get(guild.roles, name="Amigos Careca")
        elif payload.emoji.name == '🐰':
            role = discord.utils.get(guild.roles, name="Amigos Beatriz")
        elif payload.emoji.name == '🦋':
            role = discord.utils.get(guild.roles, name="Amigos Barbara")
        else:
            return
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        await member.add_roles(role)

"""" 
@bot.event
async def on_ready():
    message_id == 1067562113826029709:

"""

bot.run('MTA2NzUzMTY2MjYzNzkyODUyOA.GiR9h7.VIOC__YF8uTDjvCLsjtrj0RdDwlG0a2o1vl1jc')