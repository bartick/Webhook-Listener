import os
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import asyncio
import sqlite3
from dotenv import load_dotenv
from flask import Flask, request, Response

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def server():
  return "This is a web server"

@app.route('/webhook', methods=['POST'])
def response():
  """ Table Webhook (Authorization text, Server int, Webhook text) """
  conn = sqlite3.connect('database.db')
  c = conn.cursor()
  select = c.execute('''SELECT * FROM Webhook WHERE Authorization=?''',(request.headers.get('authorization'),)).fetchone()
  conn.close()
  if not select==None:
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(discord_webhook(request.json, select[2]))
    return Response(status=200)


async def discord_webhook(data, url):
  async with aiohttp.ClientSession() as session:
    auth = {"Authorization": f"Bot {os.getenv['DISCORD_AUTH']}"}
    resp = await session.get(f'https://discord.com/api/users/{data["user"]}',headers=auth)
    user = await resp.json()
    webhook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
    vote = f"**{user['username']}#{user['discriminator']}** just voted for the server.\nThank you very much for the vote <:inluv:728631587637297222>"
    avatar_url = f'https://cdn.discordapp.com/avatars/{user["id"]}/{user["avatar"]}.png?size=1024'
    await webhook.send(vote, username=user['username'], avatar_url=avatar_url)


if __name__=='__main__':
    """ MAKE SURE THE PORT YOU ARE USING IS OPEN """
    app.run(host='0.0.0.0',port=5000, debug=True)