import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram import F
from aiogram import BotCommand
from aiogram.utils import run_polling

API_TOKEN = '8084154106:AAHn3ikCWbQ8Knky3VxfujNvgu8VgFTNTWQ'  # Замените на токен Вашего бота

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")
    print("Привет! Я бот, помогающий твоему здоровью.")

# Обработчик всех остальных сообщений
@router.message(F.text)
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")
    print("Введите команду /start, чтобы начать общение.")

# Настройка диспетчера
dp = Dispatcher(storage=storage)
dp.include_router(router)

# Запуск бота
if __name__ == '__main__':
    run_polling(dp, skip_updates=True)
