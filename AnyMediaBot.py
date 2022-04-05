"""
MIT License

Copyright (c) 2022 IamNimsara

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
from pyrogram import filters, Client
import json
import requests
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

AnyMediaBot = Client(
   "Link Short Bot",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

IMG = "https://telegra.ph/file/dca764cc4a75fadfc7fde.jpg"

REPLY_MARKUP = InlineKeyboardMarkup(
    [
       [  
           InlineKeyboardButton("🍃Our Channel🍃", url="https://t.me/Dr_Stranger_Botz_Infinity")
           InlineKeyboardButton("🍂Our Group🍂", url="https://t.me/Dr_Stranger_Botz_Infinity_Chat")
           InlineKeyboardButton("⚙️DᕮᐯᕮᒪOᑭᕮR⚙️", url="https://t.me/Dr_Stranger_XD")
           InlineKeyboardButton("🧰My Source Code🧰", url="https://github.com/Dr-Stranger-Botz-Infinity/Link-Shortner-Ro-Bot")
       ],
    ]
)
START_TEXT = """
Hello 👋👋
🔅 I am a powerful Lιɳƙ Sԋσɾƚɳҽɾ Bσƚ.  Send me the long link you have. I will shorten it.  🔗 

🤷‍♂️ Help
  🔗 Link Short
    /short [Link]
   
💻Powered By @Dr_Stranger_Botz_Infinity

"""
@AnyMediaBot.on_message(filters.command("start"))
async def start(m, message):
    await message.reply_text(START_TEXT, reply_markup=REPLY_MARKUP)

@AnyMediaBot.on_message(filters.command("short"))
async def shortlink(m, message):
    if len(message.command) < 2:
            return await message.reply_text("**USE :** /short link")
    m = await message.reply_text("**short link...**")
    shortlink = message.text.split(None, 1)[1]
    shortlinkapi=json.loads(requests.get(f'https://api.g99solutions.com/linkshort?url={shortlink}').text)
    title=shortlinkapi['title']
    youlink=shortlinkapi['longurl'] 
    shortlink=shortlinkapi['shorturl']
    TEXT = f"""
◇──────────────────────────◇

◇ **{title}**

◇ **Your Link :** {youlink}

☘️ **Short Link :** {shortlink}

◇──────────────────────────◇
"""
    await message.reply_text(TEXT, reply_markup=REPLY_MARKUP)
    await m.delete()

print("""
Bot Alive!
"""
)
AnyMediaBot.run()
