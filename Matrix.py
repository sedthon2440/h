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

from telethon import TelegramClient, events, Button
import asyncio

# بيانات الدخول للبوت 
api_id = '17211426'
api_hash = '656a097533402eb717ba82298a752177'
bot_token = '7279617579:AAH05WmgKb6WhGJL9x2tGRy9RvqSA6eKpZ8'

# إنشاء عميل تيلثون
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond("مرحبا! 👋")

    # إنشاء الكيبورد
    buttons = [
        [Button.inline("زر 1", data="button1"), Button.inline("زر 2", data="button2")],
        [Button.inline("زر 3", data="button3")]
    ]

    # إرسال الكيبورد
    await event.respond("اختر زرًا من الكيبورد:", buttons=buttons)

@client.on(events.CallbackQuery(data='button1'))
async def button1_handler(event):
    await event.edit("أنت ضغطت على زر 1!")

@client.on(events.CallbackQuery(data='button2'))
async def button2_handler(event):
    await event.edit("أنت ضغطت على زر 2!")

@client.on(events.CallbackQuery(data='button3'))
async def button3_handler(event):
    await event.edit("أنت ضغطت على زر 3!")

async def main():
    await client.start()
    print("البوت جاهز للعمل")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())

