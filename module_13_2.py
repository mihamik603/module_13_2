import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram import F
from aiogram import BotCommand
from aiogram.utils import run_polling

API_TOKEN = '&&&' 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")
    print("Привет! Я бот, помогающий твоему здоровью.")

@router.message(F.text)
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")
    print("Введите команду /start, чтобы начать общение.")

dp = Dispatcher(storage=storage)
dp.include_router(router)

if __name__ == '__main__':
    run_polling(dp, skip_updates=True)
