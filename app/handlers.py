from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.buttons as st
from Google_Translater import translate as tr

router = Router()


@router.message(CommandStart())
async def startCmd(message: Message):
    await message.reply(f"Привет\n{message.from_user.id}\n {message.from_user.first_name}\n{message.from_user.username}")


@router.message()
async def CheckFText(message: Message):
    await message.answer(message.text, reply_markup=st.setting)
    message_id = message.message_id


@router.callback_query(F.data == "ru")
async def ru_selection(callback: CallbackQuery):
    print("hleb 3")
    message = await callback.message.chat.get_message(callback.message.message_id)
    # Переводим текст на русский
    print("hleb 4")
    translated_text = tr.translate(message.text, dest='ru')
    # Редактируем сообщение с переводом
    print("hleb 5")
    await callback.message.edit_text(translated_text)
    print("hleb 6")


@router.callback_query(F.data == "eng")
async def ru(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Английский")


@router.callback_query(F.data == "ky")
async def ru(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("Кыргызский")
