from typing import Union

from telebot.apihelper import ApiTelegramException

from bot_initializer import bot
from const_package import const, endpoints, messages
from utils.button_helper import make_buttons
from utils.requests_helper import get_upcoming_movies, search_movie


def send_main_menu(chat_id: Union[str, int], lang: str):
    rkm = make_buttons(const.MENU_LIST, lang)
    bot.send_message(chat_id, const.MAIN_MENU[lang], reply_markup=rkm)


def send_upcoming_movies(chat_id: Union[str, int], lang: str):
    upcoming_movies = get_upcoming_movies(lang)['results']
    for upcoming_movie in upcoming_movies:
        send_upcoming_movie_message(upcoming_movie, chat_id)


def send_upcoming_movie_message(upcoming_movie, chat_id: Union[str, int]):
    message = f"*{upcoming_movie['original_title']}* ({upcoming_movie['title']})"
    message += f"\n\n📅: {upcoming_movie['release_date']}"
    message += f"\n\n{upcoming_movie['overview']}"
    image_path = f"{endpoints.IMAGE_BASE_URL}w500{upcoming_movie['poster_path']}"
    try:
        bot.send_photo(chat_id, image_path, message, "Markdown")
    except ApiTelegramException:
        message += f"\n\n🖼 -> [IMAGE]({image_path})"
        bot.send_message(chat_id, message, "Markdown")


def send_search_text_message(chat_id: Union[str, int], lang: str):
    rkm = make_buttons([const.BACK[lang]])
    bot.send_message(chat_id, messages.ENTER_TEXT[lang], reply_markup=rkm)


def send_searching_movies(chat_id: Union[str, int], query: str, lang: str):
    search_result = search_movie(query, lang)
    bot.send_message(chat_id, messages.SEARCH_RESULT[lang].format(count=search_result['total_results']))
    for searching_movie in search_result['results']:
        send_searching_movie_message(searching_movie, chat_id)


def send_searching_movie_message(searching_movie, chat_id: Union[str, int]):
    message = f"*{searching_movie['original_title']}* ({searching_movie['title']})"
    message += f"\n\n📅: {searching_movie['release_date']}"
    message += f"\n\n{searching_movie['overview']}"
    image_path = f"{endpoints.IMAGE_BASE_URL}w500{searching_movie['poster_path']}"
    try:
        bot.send_photo(chat_id, image_path, message, "Markdown")
    except ApiTelegramException:
        message += f"\n\n🖼 -> [IMAGE]({image_path})"
        bot.send_message(chat_id, message, "Markdown")


def send_selection_language(chat_id):
    rkm = make_buttons(const.LANGUAGES_LIST)
    bot.send_message(chat_id, messages.CHOOSE_LANGUAGE, reply_markup=rkm)


def send_contact_message(chat_id: Union[str, int], lang: str):
    bot.send_message(chat_id, messages.CONTACT_MESSAGE[lang])


def send_error_with_uz(chat_id):
    bot.send_message(chat_id, messages.ERROR_WITH_UZ)
