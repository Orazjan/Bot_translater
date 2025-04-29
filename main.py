import asyncio

from aiogram import Bot, Dispatcher
from environs import Env
import logging
from app.handlers import router

env = Env()
env.read_env()

bot = Bot(token=env.str('TOKEN'))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
