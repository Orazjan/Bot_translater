import asyncio
from googletrans import Translator


async def detect_language(text):
    translator = Translator()
    return await translator.detect(text)


async def translate(text, src, dest):
    translator = Translator()

    translation = await translator.translate(text, src=src, dest=dest)
    print(f"{translation.text}")

    return translation.text
