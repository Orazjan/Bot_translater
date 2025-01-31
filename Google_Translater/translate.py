import asyncio
from googletrans import Translator


async def translate(text, dest):
    translator = Translator()

    # Detect language
    detected_language = await translator.detect(text)
    print(f"Обнаруженный язык: {detected_language}")
    print("hleb 1")
    # Translate to Russian
    translation = await translator.translate(text, src=detected_language.lang, dest=dest)
    print(f"Перевод на русский: {translation.text}")
    print("hleb 2")
    return translation
