import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import random

BOT_TOKEN = 'YOUR_BOT_TOKEN'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def simple_rhyme(text):
    words = text.split()
    if len(words) < 2:
        return "Текст слишком короткий для рифмы."
    
    last_word = words[-1].lower()
    rhyme_endings = ['ать', 'еть', 'ить', 'оть', 'уть', 'ыть', 'ять']
    
    for ending in rhyme_endings:
        if last_word.endswith(ending):
            rhyme_word = random.choice(['кровать', 'медведь', 'любить', 'полоть', 'гнуть', 'быть', 'взять'])
            return f"{text}\nА в ответ звучит: {rhyme_word}!"
    
    return f"{text}\nРифма не найдена, но звучит красиво!"

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот, который пытается рифмовать ваши сообщения. Просто отправьте мне текст, и я попробую его зарифмовать.")

@dp.message()
async def rhyme_message(message: types.Message):
    rhymed_text = simple_rhyme(message.text)
    await message.answer(rhymed_text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())