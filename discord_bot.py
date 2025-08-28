import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']
import discord
from dotenv import dotenv_values #this to store tokem
config=dotenv_values(".env")
TOKEN= config["DISCORD_TOKEN"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Prevent the bot from responding to itself
        if message.author == self.user:
            return

        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())

# Enable intents
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

# ⚠️ Don't share your real token publicly!
client.run(TOKEN)
