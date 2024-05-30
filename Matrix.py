from time import sleep
import logging
import asyncio
import time
import datetime
import os
import requests
import re
import random
import telethon
from telethon import events, TelegramClient, functions
from telethon.tl import functions, types
from telethon.tl.types import InputPeerUser
from telethon.errors import FloodWaitError
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
    UserNotParticipantError
)
from telethon.sessions import StringSession
from telethon.utils import get_display_name
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import (
    ImportChatInviteRequest as Get,
    GetHistoryRequest,
    ImportChatInviteRequest,
    GetMessagesViewsRequest
)
from telethon.tl.functions.channels import (
    LeaveChannelRequest,
    JoinChannelRequest,
    InviteToChannelRequest,
    GetParticipantRequest
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import (
    SendVoteRequest,
    SendReactionRequest
)




app_id = os.environ.get("APP_ID")
app_hash = os.environ.get("APP_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")



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
