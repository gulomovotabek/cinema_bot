import telebot

from const_package import credentials
from database import initialize


bot = telebot.TeleBot(credentials.BOT_TOKEN)
initialize()
