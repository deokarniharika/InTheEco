import discord
import os
import requests
import praw

from bs4 import BeautifulSoup
from keep_alive import keep_alive

with open('id.txt', 'r') as f:
    CLIENT_ID = f.read()

with open('secret.txt', 'r') as f:
    SECRET_KEY = f.read()

#dictionary where we specify every step
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY,
                     user_agent='MyAPI/0.0.1')

#scraping data from the envrionment subreddit and getting the top 10 posts as the output.

evs_posts = reddit.subreddit('environment').top(limit=20)

for post in evs_posts:
    sky = post.title

client = discord.Client()


def recent_score():
    s2 = sky
    embed = discord.Embed(title="Top Environmental News: ",
                          description=s2,
                          color=0x71BC68)
    return embed


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!top'):
        embed = recent_score()
        await message.channel.send(embed=embed)


my_secret = os.environ['TOKEN']

keep_alive()
client.run(my_secret)
