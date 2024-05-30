import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters



load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 17211426))
API_HASH = getenv("API_HASH", "656a097533402eb717ba82298a752177")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://proceed58:proceed58@cluster0.p5s9ym5.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2000))

# Chat id of a group for logging bot's activities
