import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if message.content.startswith('$inspire'):
        await message.channel.send(get_quote())

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.channel.startswith('$poop'):
        await message.channel.send(':poop:')

client.run("")