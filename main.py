import discord
from textgenrnn import textgenrnn

textgen = textgenrnn()
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    f = open("message.txt", mode="a", encoding="utf-8")
    f.write(message.content + "\n")
    f.close()

    if message.author == client.user:
        return

    if message.content.startswith('&gen'):
        await message.channel.send("Generating message ! please wait...")
        await message.channel.send(textgen.generate(return_as_list=True)[0])


client.run("Token here
