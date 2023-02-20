from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def make_buttons(buttons_list: [str], lang: str = None, count=2):
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=count)
    for button_text in buttons_list:
        if lang is None:
            rkm.add(KeyboardButton(button_text))
        else:
            rkm.add(KeyboardButton(button_text[lang]))
    return rkm
