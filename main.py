import discord
import sqlite3
import re
from setting import TOKEN


forbidden_words = [r"бл[я\*]ть"]


class KarmaBot(discord.Client):
    async def on_ready(self):
        print("Бот встал на стражу порядка кармы сервера.")

    def punishment(self, patern):
        pass

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return
        for i in forbidden_words:
            regex = re.compile(i, re.IGNORECASE)
            if regex.search(message.content):
                punishment(message.content)
                await message.channel.send("Вы, " + message.author + ", понизили свою карму")



def main():
    intents = discord.Intents.default()
    client = KarmaBot(intents=intents)
    client.run(TOKEN)


if __name__ == '__main__':
    main()


