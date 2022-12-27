from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nДобавь новую запись в телефонную книгу!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Доступные операции с телефонной книгой:\n\
    1 - добавить номер\n\
    2 - посмотреть все записи\n\
    3 - найти контакт")