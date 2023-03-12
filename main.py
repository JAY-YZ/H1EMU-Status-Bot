import discord
import requests
from bs4 import BeautifulSoup
import asyncio

client = discord.Client()

async def update_status():
    while True:
        try:
            response = requests.get("https://serverlist.h1emu.com/us/")
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.find('table')
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                columns = [col.text.strip() for col in columns]
                if len(columns) >= 2 and columns[1] == 'YOUR SERVER NAME EXACTLY HOW IT SHOWS ON THE H1EMU SERVER LIST':
                    status = columns[4]
                    await client.change_presence(activity=discord.Game(name=f"{status} online"))
                    break
        except:
            pass
        await asyncio.sleep(30)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    client.loop.create_task(update_status())

client.run("YOURTOKEN")
