import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import aiohttp

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, который отправляет картинки с котиками. Используй команду /cat, чтобы получить случайную картинку котика.")

# Обработчик команды /cat
@dp.message(Command("cat"))
async def cmd_cat(message: types.Message):
    try:
        # Получаем случайную картинку котика с API
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.thecatapi.com/v1/images/search') as response:
                data = await response.json()
                cat_url = data[0]['url']
        
        # Отправляем картинку пользователю
        await message.answer_photo(cat_url, caption="Вот ваш котик! 😺")
    except Exception as e:
        logging.error(f"Ошибка при получении картинки котика: {e}")
        await message.answer("Извините, не удалось получить картинку котика. Попробуйте позже.")

# Функция для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
