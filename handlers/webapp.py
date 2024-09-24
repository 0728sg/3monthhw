from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


async def reply_webapp(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)

    instagram = KeyboardButton('Instagram',
                                  web_app=types.WebAppInfo(url="https://www.instagram.com"))

    ts_kg = KeyboardButton('TS.kg',
                           web_app=types.WebAppInfo(url="https://www.ts.kg/"))

    lehigh = KeyboardButton('Lehigh',
                            web_app=types.WebAppInfo(url="https://www2.lehigh.edu/"))

    steam = KeyboardButton('Steam',
                           web_app=types.WebAppInfo(url="https://store.steampowered.com/"))

    ubisoft = KeyboardButton('UBISOFT',
                             web_app=types.WebAppInfo(url="https://www.ubisoft.com/"))


    keyboard.add(instagram, ts_kg, lehigh, steam, ubisoft)

    await message.answer(text='WebApp кнопки: ', reply_markup=keyboard)



def register_handlers_webapp(dp: Dispatcher):
    dp.register_message_handler(reply_webapp, commands=['reply_webapp'])