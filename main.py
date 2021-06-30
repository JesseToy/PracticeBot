import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))  

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$Time'):
    await message.channel.send('9:30 PM EST')

  if message.content.startswith('$Stream'):
    await message.channel.send('https://www.twitch.tv/toxicflexx1')

  if message.content.startswith('$Tip'):
    await message.channel.send('https://streamelements.com/toxicflexx1/tip')

client.run(os.getenv('TOKEN'))