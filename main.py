from pydub import AudioSegment
import os, time
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
dir = os.getcwd() + '/'

bot = Client(
    "voice-tag",
    bot_token = BOT_TOKEN,
    api_id = API_ID,
    api_hash = API_HASH
)

@bot.on_message(filters.video | filters.document)
async def startt(bot, m):
    a2_1 = AudioSegment.from_mp3(dir + '2.1.mp3')
    a2_2 = AudioSegment.from_mp3(dir + '2.2.mp3')
    aa2 = a2_1.append(a2_2)
    aa2.export(dir+"2.mp3", format="mp3")

    os.system('ffmpeg -i 2.mp3')

bot.run()
