from aiogram import types, Dispatcher
from config import bot, admin
from aiogram.dispatcher.filters import Command



async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)
        await message.answer("soobshenie zakrepleno")
    else:
        await message.answer("otvet na soobshenie")



async def pin_command_in_private_chat(message: types.Message):
    await message.answer("/pin")

def register_admin(dp: Dispatcher):
    dp.register_message_handler (pin_message,
                                 content_types=types.ContentType.NEW_CHAT_MEMBERS)
    dp.register_message_handler(pin_command_in_private_chat,commands=['pinned'])

    dp.register_message_handler(pin_message)