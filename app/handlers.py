from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
import app.buttons as st
from Google_Translater import translate as tr
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from app.testspeech import transcribe_voice_bytes
import io

router = Router()


class TranslationStates(StatesGroup):
    waiting_for_translation = State()


@router.message(CommandStart())
async def startCmd(message: Message):
    await message.answer(f"Привет. Вас приветствует бот-переводчик. Напишите или отправьте мне голосовое сообщение для перевода")


@router.message(F.voice)
async def handle_voice_message(message: Message, state: FSMContext):
    bot = message.bot
    file = await bot.get_file(message.voice.file_id)
    file_bytes = io.BytesIO()
    await bot.download_file(file.file_path, destination=file_bytes)
    file_bytes.seek(0)

    text = transcribe_voice_bytes(file_bytes.read())

    if not text:
        await message.answer("Язык не поддерживается или не удалось распознать.")
        return

    detected_language = await tr.detect_language(text)

    await state.update_data(text=text)
    await state.set_state(TranslationStates.waiting_for_translation)

    if detected_language.lang.lower() == "ru":
        await message.answer(text, reply_markup=st.keyboardForRu)
    elif detected_language.lang.lower() == "en":
        await message.answer(text, reply_markup=st.keyboardForEng)
    elif detected_language.lang.lower() == "ky":
        await message.answer(text, reply_markup=st.keyboardForKgz)
    else:
        await message.answer(text, reply_markup=st.keyboardForNotDetect)


@router.message()
async def choose_lang(message: Message, state: FSMContext):

    await state.update_data(text=message.text)
    await state.set_state(TranslationStates.waiting_for_translation)

    detected_language = await tr.detect_language(message.text)
    if (detected_language.lang == "ru"):
        await message.answer(message.text, reply_markup=st.keyboardForRu)
    elif (detected_language.lang == "en"):
        await message.answer(message.text, reply_markup=st.keyboardForEng)
    elif (detected_language.lang == "ky"):
        await message.answer(message.text, reply_markup=st.keyboardForKgz)
    else:
        await message.answer(message.text, reply_markup=st.keyboardForNotDetect)


@router.callback_query(
    F.data.in_({"ru", "en", "ky"}),
    TranslationStates.waiting_for_translation
)
async def handle_translation_selection(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    text_to_translate = user_data.get("text")

    target_lang = callback.data

    translated_text = await tr.translate(text_to_translate, src="auto", dest=target_lang)

    await callback.message.edit_text(translated_text)
    await callback.answer()

    await state.clear()
