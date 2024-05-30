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

# تعريف المتغيرات
api_id = '17211426'
api_hash = '656a097533402eb717ba82298a752177'
bot_token = '7228727354:AAHz0jKXeppjXTP_P2UBUh-2VNY-bOchXxs'

# إنشاء العميل
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

# دالة للرد على الرسائل مع الأزرار
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    buttons = [
        [Button.inline('Button 1', b'btn1')],
        [Button.inline('Button 2', b'btn2')]
    ]
    await event.respond('Choose an option:', buttons=buttons)

# دالة للتعامل مع الضغط على الأزرار
@client.on(events.CallbackQuery(data=b'المطور'))
async def button1(event):
    await event.edit('≭︰Dev Name ↬ ⦗ اެنِهِيَاެࢪ بَذِاެكَࢪهِ ⦘\n≭︰Dev User ↬ ⦗ @Yll9ll ⦘\n≭︰Dev id ↬ ⦗ 6723988021 ⦘')

@client.on(events.CallbackQuery(data=b'قناه السورس'))
async def button2(event):
    await event.edit('@VEEVVW')

# تشغيل البوت
client.start()
client.run_until_disconnected()



