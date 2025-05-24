import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN


from googletrans import Translator

from gtts import gTTS
import os
import random
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()

@dp.message(Command('start'))
async def start_handler(message: Message):
    await message.answer("Выберите команду:", reply_markup=kb.main)

@dp.message(F.text == "Привет")
async def say_hello(message: Message):
    user_name = message.from_user.first_name
    await message.answer(f"Привет, {user_name}!")

@dp.message(F.text == "Пока")
async def say_goodbye(message: Message):
    user_name = message.from_user.first_name
    await message.answer(f"До свидания, {user_name}!")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}", reply_markup=kb.main)

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}", reply_markup=kb.links)

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}", reply_markup=kb.inline_keyboard)

@dp.callback_query(F.data == "more")
async def more(callback: CallbackQuery):
    await callback.message.answer('Вот две опции', reply_markup=await kb.test_inline())

@dp.message(F.text == "Опция 1")
async def option_1(message: Message):
    await message.answer("Тестовая информация первой опции")

@dp.message(F.text == "Опция 2")
async def option_2(message: Message):
    await message.answer("Тестовая информация второй опции")

#edit_text

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


