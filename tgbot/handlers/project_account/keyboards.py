from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)


def send_proj_mode_keyboard() ->InlineKeyboardMarkup:
    buttons = [[InlineKeyboardButton(text=c, callback_data=c) for c in ('ссылка', 'фото', 'отмена')]]
    return InlineKeyboardMarkup(buttons)

