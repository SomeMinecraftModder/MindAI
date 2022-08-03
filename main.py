#!/bin/python
import discord
from textgenrnn import textgenrnn

textgen = textgenrnn()
client = discord.Client()

bot = discord.Bot(debug_guild=826685556431912961)

#Commented out because I don't know the on_ready function call for the py-cord API
""";
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
"""

@bot.slash_command(name="message")
async def on_message(ctx, message: str):
	f = open("message.txt", mode="a", encoding="utf-8")
	f.write(message + "\n")
	f.close()

@bot.slash_command(name="gen")
async def gen(ctx):
	await ctx.defer()
	await ctx.followup.send("Generating message ! please wait...")
	await ctx.followup.send(textgen.generate(return_as_list=True)[0])


client.run("replace me")
