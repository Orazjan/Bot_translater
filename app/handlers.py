from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.buttons as st
from Google_Translater import translate as tr
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

router = Router()


class TranslationStates(StatesGroup):
    waiting_for_translation = State()


@router.message(CommandStart())
async def startCmd(message: Message):
    await message.answer(f"Привет. Вас приветствует бот-переводчик. Напишите мне для перевода")


@router.message()
async def choose_lang(message: Message, state: FSMContext):

    await state.update_data(text=message.text)
    await state.set_state(TranslationStates.waiting_for_translation)

    detected_language = await tr.detect_language(message.text)
    print(detected_language.lang)
    if (detected_language.lang == "ru"):
        await message.answer(message.text, reply_markup=st.keyboardForRu)
    elif (detected_language.lang == "en"):
        await message.answer(message.text, reply_markup=st.keyboardForEng)
    elif (detected_language.lang == "ky"):
        await message.answer(message.text, reply_markup=st.keyboardForKgz)


# Обработчик callback-запроса для перевода на русский
@router.callback_query(F.data == "ru", TranslationStates.waiting_for_translation)
async def ru_selection(callback: CallbackQuery, state: FSMContext):
    # Получаем сохраненный текст из состояния
    user_data = await state.get_data()
    text_to_translate = user_data.get("text")

    # Выполняем перевод
    translated_text = await tr.translate(text_to_translate, src="auto", dest="ru")

    # Отправляем переведенный текст
    await callback.message.edit_text(translated_text)
    await callback.answer()

    # Сбрасываем состояние
    await state.clear()


@router.callback_query(F.data == "en", TranslationStates.waiting_for_translation)
async def en_selection(callback: CallbackQuery, state: FSMContext):
    # Получаем сохраненный текст из состояния
    user_data = await state.get_data()
    text_to_translate = user_data.get("text")

    # Выполняем перевод
    translated_text = await tr.translate(text_to_translate, src="auto", dest="en")

    # Отправляем переведенный текст
    await callback.message.edit_text(translated_text)
    await callback.answer()

    # Сбрасываем состояние
    await state.clear()


@router.callback_query(F.data == "ky", TranslationStates.waiting_for_translation)
async def ky_selection(callback: CallbackQuery, state: FSMContext):
    # Получаем сохраненный текст из состояния
    user_data = await state.get_data()
    text_to_translate = user_data.get("text")

    # Выполняем перевод
    translated_text = await tr.translate(text_to_translate, src="auto", dest="ky")

    # Отправляем переведенный текст
    await callback.message.edit_text(translated_text)
    await callback.answer()

    # Сбрасываем состояние
    await state.clear()
