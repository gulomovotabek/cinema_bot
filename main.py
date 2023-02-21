import telebot

from bot_initializer import bot
from database import db
from database.models import User
from states import State
from database import redis_helper
from const_package import const, messages
from utils import send_message


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    if db.is_user_exists(message.chat.id):
        user = db.get_user_by_tg_id(message.chat.id)
        redis_helper.set_to_redis(message.chat.id, user.lang)
        send_message.send_main_menu(message.chat.id, user.lang)
        bot.set_state(message.chat.id, State.Menu)
    else:
        bot.reply_to(message, messages.WELCOME_MESSAGE)
        send_message.send_selection_language(message.chat.id)
        bot.set_state(message.chat.id, State.LanguageSelection)
        db.create_user(User.create_from_tg_user(message.from_user))


@bot.message_handler(state=State.Menu)
def menu_handler(message: telebot.types.Message):
    lang = redis_helper.get_lang(message.chat.id)
    if message.text == const.UPCOMING_MOVIES[lang]:
        send_message.send_upcoming_movies(message.chat.id, lang)
    elif message.text == const.SEARCH[lang]:
        send_message.send_search_text_message(message.chat.id, lang)
        bot.set_state(message.chat.id, State.Search)
    elif message.text == const.CHANGE_LANGUAGE[lang]:
        send_message.send_selection_language(message.chat.id)
        bot.set_state(message.chat.id, State.LanguageSelection)
    elif message.text == const.CONTACT[lang]:
        send_message.send_contact_message(message.chat.id, lang)
    else:
        bot.send_message(message.chat.id, "Not implemented!")


@bot.message_handler(state=State.Search)
def search_movie_handler(message: telebot.types.Message):
    lang = redis_helper.get_lang(message.chat.id)
    if message.text == const.BACK[lang]:
        send_message.send_main_menu(message.chat.id, lang)
        bot.set_state(message.chat.id, State.Menu)
    else:
        send_message.send_searching_movies(message.chat.id, message.text, lang)


@bot.message_handler(state=State.LanguageSelection)
def change_language(message: telebot.types.Message):
    lang = const.EN
    if message.text not in const.LANGUAGES_LIST:
        bot.send_message(message.chat.id, "Try again!")
        return
    elif message.text == const.ENGLISH:
        lang = const.EN
    elif message.text == const.RUSSIAN:
        lang = const.RU
    elif message.text == const.UZBEK:
        send_message.send_error_with_uz(message.chat.id)
        lang = const.UZ
    send_message.send_main_menu(message.chat.id, lang)
    redis_helper.set_to_redis(message.chat.id, lang)
    bot.set_state(message.chat.id, State.Menu)
    db.update_user(message.chat.id, {'language': lang})


bot.add_custom_filter(telebot.custom_filters.StateFilter(bot))
bot.polling(True)
