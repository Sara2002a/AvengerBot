import sys
import dns.resolver

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pymongo import MongoClient
from pyrogram import Client
from pyromod import listen

from config import config
from Avenger.AvengerGban import AvengerClient

OWNER_ID = config.settings.owner
BOT_ID = config.telegram.bot.id
BOT_NAME = config.telegram.bot.name
BOT_USERNAME = config.telegram.bot.username
LOG_CHANNEL = config.settings.log.chat_id
SUDO_USERS = config.settings.sudo_users
PREFIX = config.settings.commands.prefix
BACKUP_CHAT = config.settings.backup.chat_id

AvengerCli = Client(
    session_name='AvengerSession',
    api_id=config.telegram.api_id,
    api_hash=config.telegram.api_hash,
    bot_token=config.telegram.bot.token
)

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] 

AvengerAPI = AvengerClient(api_key=config.api.avenger.api_key)

scheduler = AsyncIOScheduler()

try:
  AvengerMongoClient = MongoClient(config.database.database_url)
  AvengerDB = AvengerMongoClient.avenger_mongo
except:
  sys.exit(f"{BOT_NAME}'s database is not running!")

TELEGRAM_SERVICES_IDs = (
    [
        777000,
        1087968824
    ]
)

GROUP_ANONYMOUS_BOT = 1087968824
