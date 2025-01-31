from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

setting = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Русский', callback_data="ru")],
                     [InlineKeyboardButton(
                         text='Кыргызский', callback_data='ky')],
                     [InlineKeyboardButton(
                         text='Английский', callback_data='eng')]
                     ])
