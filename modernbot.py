import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from config import TOKEN


from googletrans import Translator  

from gtts import gTTS
import os
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()


@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('sample-5s.mp4')
    await bot.send_video(message.chat.id, video)

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile('1718883178_sample4.ogg')
    await message.answer_voice(voice)

@dp.message(Command('doc'))
async def doc(message: Message):
    doc = FSInputFile('Еще один важный файл.pdf')
    await bot.send_document(message.chat.id, doc)

@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile('sample-3s.mp3')
    await bot.send_audio(message.chat.id, audio)

@dp.message(Command('training'))
async def training(message: Message):
    training_list = [
        '1. Приседания - Описание: \n  Стойте прямо, ноги на ширине плеч. Опускайтесь в присед, как будто садитесь на стул, затем поднимитесь обратно. \n - Повторения: \n 3 подхода по 12-15 раз.'
        '2. Отжимания - Описание: \n  Лягте на живот, руки на ширине плеч. Поднимайте тело, опираясь на руки и носки ног, затем опуститесь обратно. \n - Повторения: \n 3 подхода по 8-12 раз. (Если сложно, можно делать отжимания с колен).'
        '3. Планка - Описание: \n Примите упор лежа, опираясь на предплечья и носки ног. Держите тело в прямой линии, напрягая пресс и ягодицы. \n - Время:  3 подхода по 30-60 секунд.'
    ]
    rand_tr = random.choice(training_list)
    await  message.answer(f'Это ваша тренировка на сегодня {rand_tr}')
    tts = gTTS(text=rand_tr, lang='ru')
    tts.save('training.ogg')
    audio = FSInputFile('training.ogg')
    await bot.send_voice(message.chat.id, audio)
    os.remove('training.ogg')

@dp.message(Command('photo', prefix='&'))
async def photo(message: Message):
    list = ["https://img.freepik.com/free-photo/close-up-adorable-kitten-couch_23-2150782439.jpg",
            "https://t4.ftcdn.net/jpg/05/80/42/17/360_F_580421779_G5tb5Zrf4TvyI0PbCPOhZmMfn17MBE70.jpg",
            "https://kartinki.pics/uploads/posts/2022-02/thumbs/1644872555_2-kartinkin-net-p-kotiki-kartinki-2.jpg"
    ]
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption="Это супер крутая фотка!")

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ["Ого какая фотка", "Непонятно что это такое", "Не отправляй мне больше такое"]
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1],destination=f'tmp/{message.photo[-1].file_id}.jpg')

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Иску́сственный интелле́кт (англ. artificial intelligence; AI) в самом широком смысле — это интеллект, демонстрируемый машинами, в частности компьютерными системами. Это область исследований в области компьютерных наук, которая разрабатывает и изучает методы и программное обеспечение, позволяющие машинам воспринимать окружающую среду и использовать обучение и интеллект для выполнения действий, которые максимально увеличивают их шансы на достижение поставленных целей[3')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name} ")

@dp.message()
async def start(message: Message):
    if message.text.lower() == 'тест':
        await message.answer('тестируем')

@dp.message()
async def translate_message(message: Message):
    translated = translator.translate(message.text, src='ru', dest='en')
    await message.answer(f'Переведенный текст: {translated.text}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


