import discord
import sqlite3
import re
import argparse
from setting import TOKEN


forbidden_words = {}


class KarmaBot(discord.Client):
    async def on_ready(self):
        print("Бот встал на стражу порядка кармы сервера.")



def main():
    intents = discord.Intents.default()
    client = KarmaBot(intents=intents)
    client.run(TOKEN)


if __name__ == '__main__':
    main()


