import discord
#from discord.ext import commands
import os
import requests
import json
from deep_translator import GoogleTranslator
from ar_or_en import ar_or_en
from ar_or_en import ar_or_en0
from translate import translate_ar
from translate import translate_en
from translate import translate_ar0
from translate import translate_en0
from keep_alive import keep_alive
from dic import automatic_reply
#from music_cog import music_cog
#from replit import db

client = discord.Client()


def get_json_data():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    return (json_data)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    y = message.content
    msg = y.lower()

    if (msg.startswith(">>translate ")) or (msg.startswith(">>tr ")):
        if ar_or_en(msg) == 1:
            await message.channel.send(translate_en(msg))
        elif ar_or_en(msg) == 2:
            await message.channel.send(translate_ar(msg))
        elif ar_or_en(msg) == 3:
            await message.channel.send(
                "خطأ!!! يحتوي النص المرسل على مزيج من لغتين \nerror!!! The sent text contains a mixture of two languages"
            )
        await message.channel.send(file=discord.File('pencil.png'))

    if message.channel == "ar-⇋-en":
        if ar_or_en0(msg) == 1:
            await message.channel.send(translate_en0(msg))
        elif ar_or_en0(msg) == 2:
            await message.channel.send(translate_ar0(msg))
        elif ar_or_en0(msg) == 3:
            await message.channel.send(
                "خطأ!!! يحتوي النص المرسل على مزيج من لغتين \nerror!!! The sent text contains a mixture of two languages"
            )
        await message.channel.send(file=discord.File('pencil.png'))

    if (msg == (">>quotation")) or (msg == (">>q")):
        json_data = get_json_data()
        quotation = json_data[0]['q'] + " -" + json_data[0]['a']
        tr_quotation = GoogleTranslator(source='auto', target='ar').translate(
            json_data[0]['q']) + " -" + json_data[0]['a']
        await message.channel.send(quotation)
        await message.channel.send(
            "----------------------------------------------------------")
        await message.channel.send(tr_quotation)

    if (msg in automatic_reply()):
        await message.channel.send(automatic_reply().get(msg))

    if (msg == ("0")):
        #await message.channel.send(message.author)
        await message.channel.send(message.channel)
        #channel = client.get_channel(820646736493936661)
        #await channel.send('hello')


keep_alive()
client.run(os.getenv('TOKEN'))
