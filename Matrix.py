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

from telethon import TelegramClient, events
from telethon.tl.custom import Button

# تعريف الأمر /start
async def start(event):
    # إنشاء اللوحة المفاتيح حسب ترتيبك
    button1 = Button.text('Option 1')
    button2 = Button.text('Option 2')
    button3 = Button.text('Option 3')
    button4 = Button.text('Option 4')
    button5 = Button.text('Option 5')
    button6 = Button.text('Option 6')
    button7 = Button.text('Option 7')
    button8 = Button.text('Option 8')
    keyboard = [
        [button1, button2],
        [button3, button4],
        [button5, button6],
        [button7, button8]
    ]
    # إرسال اللوحة المفاتيح كرسالة
    await event.respond('Please select an option:', buttons=keyboard)

# تعريف الردود على الأزرار
async def handle_button(event):
    if event.text == 'Option 1':
        await event.respond('You selected Option 1')
    elif event.text == 'Option 2':
        await event.respond('You selected Option 2')
    elif event.text == 'Option 3':
        await event.respond('You selected Option 3')
        elif event.text == 'Option 4':
        await event.respond('You selected Option 4')
    elif event.text == 'Option 5':
        await event.respond('You selected Option 5')
elif event.text == 'Option 6':
        await event.respond('You selected Option 6')
elif event.text == 'Option 7':
        await event.respond('You selected Option 7')
elif event.text == 'Option 8':
        await event.respond('You selected Option 8')

# تهيئة البوت وإضافة المعالج (handler)
api_id = '17211426'
api_hash = '656a097533402eb717ba82298a752177'
bot_token = '7279617579:AAH05WmgKb6WhGJL9x2tGRy9RvqSA6eKpZ8'
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
    await start(event)

@client.on(events.NewMessage(pattern='Option 1|Option 2|Option 3|Option 4|Option 5|Option 6|Option 7|Option 8|Option'))
async def handler(event):
    await handle_button(event)

# تشغيل البوت
client.run_until_disconnected()
