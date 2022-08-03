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

@bot.event
async def on_message(message: str):
	f = open("message.txt", mode="a", encoding="utf-8")
	f.write(message.content + "\n")
	f.close()

@bot.slash_command(name="gen")
async def gen(ctx):
	await message.channel.send("Generating message ! please wait...")
	await message.channel.send(textgen.generate(return_as_list=True)[0])


client.run("ODQzMjE1MzI4MzU5MzUwMzIy.GWRaPM.cM9I6dsBkZSZMT5duZAlyzyi23uUHDz_HTEMxI")
