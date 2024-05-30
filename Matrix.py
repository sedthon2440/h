import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from MatrixMusic import app
import asyncio
import requests
import config
import random
import time
from config import START_IMG_URL
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint


REPLY_MESSAGE = "<b>- اهلا بك عزيزي اليك قائمه الاوامر</b>"




REPLY_MESSAGE_BUTTONS = [

          [

             ("‹ غنيلي ›"),

             ("‹ شعر ›")
          ],

          [

             ("‹ صور ›"),

             ("‹ انمي ›")

          ],

          [

             ("‹ متحركة ›"),

             ("‹ اقتباسات ›")

          ],

          [

             ("‹ افتارات شباب ›"),

             ("‹ افتار بنات ›")

          ],

          [

             ("‹ هيدرات ›"),

             ("‹ قران ›")

          ],
    
          [

            ("‹ جداريات ›"),

            ("‹ لوكيت ›")
              
          ],
          [
            ("‹ افتارات سينمائية ›"),

            ("‹ افتارات فنانين ›")
              
          ],
          [
            ("‹ افلام ›"),

            ("‹ قيفات كوكسال ›")
              
          ],
          [
            ("‹ قيفات شباب ›"),

            ("‹ قيفات بنات ›")
              
          ],
          [
            ("‹ قيفات قطط ›"),

            ("‹ قيفات اطفال ›")
              
          ],
          [
            ("‹ قيفات رومانسية ›"),

            ("‹ قيفات كيبوب ›")
          ],
          [
             ("‹ اخفاء الكيبورد ›")

          ]

]




  

@app.on_message(filters.regex("^/start$") & filters.private)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("‹ اخفاء الكيبورد ›") & filters.private)
async def down(client, message):
          m = await message.reply("<b>- تم اغلاق الكيبورد.</b>", reply_markup= ReplyKeyboardRemove(selective=True))
