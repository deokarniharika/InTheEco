import discord
import os
import requests
from keep_alive import keep_alive
import praw

client = discord.Client()

with open('id.txt', 'r') as f:
    CLIENT_ID = f.read()

with open('secret.txt', 'r') as f:
    SECRET_KEY = f.read()

#dictionary where we specify every step
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET_KEY,
                     user_agent='MyAPI/0.0.1')

#scraping data from the envrionment subreddit and getting the top 10 posts as the output.

evs_posts1 = reddit.subreddit('environment').top(limit=20)
evs_posts2 = reddit.subreddit('environment').new(limit=20)
evs_posts3 = reddit.subreddit('environment').rising(limit=20)

#for loop used here as the evs_posts1, the ListingGenerator object has no attribute 'title'

for post in evs_posts1:
    t1 = post.title
    u1 = post.url

for post in evs_posts2:
    t2 = post.title
    u2 = post.url

for post in evs_posts3:
    t3 = post.title
    u3 = post.url


def top_news():
    embed1 = discord.Embed(title="Environmental News:",
                           description=t1,
                           url=u1,
                           color=0x71BC68)
    return (embed1.set_footer(text="Category: Top"))


def new_news():
    embed1 = discord.Embed(title="Environmental News:",
                           description=t2,
                           url=u2,
                           color=0xacd1af)
    return (embed1.set_footer(text="Category: New"))


def hot_news():
    embed1 = discord.Embed(title="Environmental News:",
                           description=t3,
                           url=u3,
                           color=0x00783e)
    return (embed1.set_footer(text="Category: Rising"))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-top'):
        embed = top_news()
        await message.channel.send(embed=embed)

    if message.content.startswith('-new'):
        embed = new_news()
        await message.channel.send(embed=embed)

    if message.content.startswith('-rising'):
        embed = hot_news()
        await message.channel.send(embed=embed)


my_secret = os.environ['TOKEN']

keep_alive()
client.run(my_secret)
