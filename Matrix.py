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

from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
YOUR_BOT_TOKEN = '7279617579:AAH05WmgKb6WhGJL9x2tGRy9RvqSA6eKpZ8' 
# تعريف الأمر /start
def start(update, context):
    # قائمة الأزرار في اللوحة المفاتيح
    button = KeyboardButton(text="Press me!")
    keyboard = [[button]]
    # تفعيل اللوحة المفاتيح وإرسالها كرسالة
    update.message.reply_text('Please press the button:', reply_markup=ReplyKeyboardMarkup(keyboard))

# تعريف الدالة التي تتعامل مع الرسائل النصية
def handle_message(update, context):
    # استلام النص المدخل من المستخدم
    text = update.message.text
    # إرسال رسالة بالنص المدخل
    update.message.reply_text(f'You entered: {text}')

# تهيئة البوت وإضافة المعالجات (handlers)
updater = Updater('YOUR_BOT_TOKEN', use_context=True)
dispatcher = updater.dispatcher

# إضافة المعالج (handler) للأمر /start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# إضافة المعالج (handler) للرسائل النصية
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
dispatcher.add_handler(message_handler)

# تشغيل البوت
updater.start_polling()


