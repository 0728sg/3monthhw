import logging
from aiogram.utils import executor
from buttons import start, start_test
from config import bot, dp, admin
from handlers import commands, echo, quiz, callback, game, store
from db import db_main

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               reply_markup=start)
        await db_main.sql_create()

commands.register_commands(dp)
quiz.register_quiz(dp)
callback.register_handlers_quiz(dp)
game.register_handlers_common(dp)
store.register_store(dp)

echo.register_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
