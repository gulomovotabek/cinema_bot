import telebot

from const_package import credentials
from database import initialize

credentials.load_env_config()
bot = telebot.TeleBot(credentials.BOT_TOKEN)
initialize()
