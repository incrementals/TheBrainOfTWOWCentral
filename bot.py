import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="b/", description="B* bot!!", intents=intents)

async def postrun(output):
    await ctx.send(output['main'])
    await ctx.author.dm_channel.send(output['pm'])