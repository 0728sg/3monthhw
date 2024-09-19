import logging
from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import os
from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = "7143396822:AAHPe-kPUtVMr6ORm-LWMCwo5G8o71M0w1Y"

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

admin = [5649689334, ]

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Hello!')
    await message.answer(text='Привет')



@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    folder = 'media'

    photo_path = os.path.join(folder, 'img.jpeg')

    with open(photo_path, 'rb') as photo:
        await message.answer_photo(photo=photo)



@dp.message_handler(commands=['mem_all'])
async def mem_all_handler(message: types.Message):
    folder = 'media'
    photos = os.listdir(folder)

    for photo_name in photos:
        photo_path = os.path.join(folder, photo_name)

        if photo_name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            with open(photo_path, 'rb') as photo:
                await bot.send_photo(message.from_user.id, photo)

@dp.message_handler(commands=['music'])
async def music_handler(message: types.Message):
    folder = 'audio'
    music_name = "track.mp3.mp3"

    music_path = os.path.join(folder, 'track.mp3.mp3')

    with open(music_path, 'rb') as music:
        await message.answer_audio(music)

@dp.message_handler(commands=['send_file'])
async def send_file_handler(message: types.Message):
    folder = 'files'
    file_name = "message.text"

    file_path = os.path.join(folder, "message.text")
    with open(file_path, 'rb') as message:
        await message.answer_files(message)



@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
