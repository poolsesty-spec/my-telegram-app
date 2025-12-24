import asyncio
import sqlite3
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# === НАСТРОЙКИ ===
API_TOKEN = '8047967212:AAH2UIo-qn7brbxLXC1kELXVvFZMwsNjwqs'
APP_URL = '- https://poolsesty-spec.github.io/my-telegram-app/' 

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN.strip(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    # Просто создаем кнопку для открытия Mini App
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌿 Открыть Eluma", web_app=WebAppInfo(url=APP_URL))]
    ])
    
    await message.answer(
        f"Привет, <b>{message.from_user.first_name}</b>! 👋\n\n"
        "Добро пожаловать в Eluma. Нажми кнопку ниже, чтобы поставить цель и составить список задач на день прямо в приложении.",
        reply_markup=kb
    )

async def main():
    print("--- Бот успешно запущен! ---")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
