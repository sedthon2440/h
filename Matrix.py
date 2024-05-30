from time import sleep
import logging
import asyncio
import time
import app
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




api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# إنشاء العميل
client = TelegramClient('session_name', api_id, api_hash).start(bot_token=bot_token)

# دالة لإرسال رسالة مع الكيبورد
async def send_with_keyboard(event):
    buttons = [
        [Button.text('Button 1'), Button.text('Button 2')],
        [Button.text('Button 3')]
    ]
    keyboard = Button.inline(buttons)
    await event.respond('Choose an option:', buttons=keyboard)

# استدعاء الدالة
with client:
    client.run_until_disconnected(send_with_keyboard)
