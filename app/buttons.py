from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

keyboardForRu = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
        text='Кыргызский', callback_data='ky')],
        [InlineKeyboardButton(
            text='Английский', callback_data='en')]
    ])

keyboardForKgz = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Русский', callback_data="ru")],
                     [InlineKeyboardButton(
                         text='Английский', callback_data='en')]
                     ])

keyboardForEng = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Русский', callback_data="ru")],
                     [InlineKeyboardButton(
                         text='Кыргызский', callback_data='ky')]
                     ])

keyboardForNotDetect = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
        text='Кыргызский', callback_data='ky')],
        [InlineKeyboardButton(
            text='Английский', callback_data='en')],
        [InlineKeyboardButton(text='Русский', callback_data="ru")]
    ])
