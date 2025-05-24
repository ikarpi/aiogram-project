from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет")],
    [KeyboardButton(text="Пока")]
], resize_keyboard=True)

links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url='https://www.google.com/search?q=%D0%B0%D0%BF%D0%BB&rlz=1C1CHNY_ru__1082__1082&oq=%D0%B0%D0%BF%D0%BB&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg70gEIMTIwNGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8&zx=1748042692600&no_sw_cr=1')],
    [InlineKeyboardButton(text="Музыка", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk')],
    [InlineKeyboardButton(text="Видео", url='https://university.zerocoder.ru/pl/teach/control/lesson/view?id=336393181&editMode=0')]
])

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Показать больше", callback_data="more")]
])

options = ["Опция 1", "Опция 2"]

async def test_inline():
    keyboard_inline = ReplyKeyboardBuilder()
    for key in options:
        keyboard_inline.add(KeyboardButton(text=key))
    return keyboard_inline.adjust(2).as_markup()