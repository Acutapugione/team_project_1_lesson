# commands.py - модуль в якому оголошені всі необхідні команди(та їх фільтри) 
from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand

FILMS_COMMAND = Command('films')
START_COMMAND = Command('start')

FILMS_BOT_COMMAND = BotCommand(command='films', description="Перегляд списку фільмів")
START_BOT_COMMAND = BotCommand(command='start', description="Почати розмову")