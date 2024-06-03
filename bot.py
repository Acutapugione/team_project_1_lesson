import asyncio
import logging
import sys
# from os import getenv
from config import BOT_TOKEN as TOKEN
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from commands import (
    FILMS_COMMAND, 
    START_COMMAND, 
    FILMS_BOT_COMMAND,
    START_BOT_COMMAND,
)
from data import get_films
from keyboards import films_keyboard_markup


dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(
        f"Вітаю, {message.from_user.full_name}!\n"\
        "Я перший бот Python розробника [ПІБ студента]."
    )


@dp.message(FILMS_COMMAND)
async def films(message: Message) -> None:
    data = get_films()
    markup = films_keyboard_markup(films_list=data)
    await message.answer(
        f"Перелік фільмів. Натисніть на назву фільму для отримання деталей.",
        reply_markup=markup
    )

# @dp.callback_query(StartCallback.filter())
# async def callb_start(callback: CallbackQuery, callback_data: StartCallback) -> None:
#     await callback.message.answer(text=f"{callback_data=}")

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await bot.set_my_commands(
        [
            FILMS_BOT_COMMAND, 
            START_BOT_COMMAND,
        ]
    )
   
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())