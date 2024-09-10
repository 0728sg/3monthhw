import logging
from aiogram.utils import executor
from buttons import start, start_test
from config import bot, dp, admin
from handlers import commands, echo, quiz, callback, game

async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               reply_markup=start)

commands.register_commands(dp)
quiz.register_quiz(dp)
callback.register_handlers_quiz(dp)
game.register_handlers_common(dp)

echo.register_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
