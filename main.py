
import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv




dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")
    await message.answer("Welcome to our bot")

@dp.message(Command(commands=["help"]))
async def reply(message: Message):
    await message.answer("I am here to assist, tell me your problem")
@dp.message(Command(commands=["hello_world"]))
async def reply(message: Message):
    await message.answer("Hello world :)")


async def main():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
    
    
