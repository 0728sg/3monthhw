from aiogram.utils import executor
from buttons import start_test
from config import bot, dp, admin
from handlers import commands, echo, quiz, callback, game, store, webapp, admin_group, send_products, send_products_delete
from db import db_main


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен!",
                               reply_markup=start_test)
        await db_main.sql_create()


commands.register_commands(dp)
quiz.register_quiz(dp)
callback.register_handlers_quiz(dp)
game.register_handlers_common(dp)
store.register_store(dp)
webapp.register_handlers_webapp(dp)
admin_group.register_admin(dp)

send_products.register_send_products_handler(dp)
send_products_delete.register_send_products_delete_handler(dp)


# echo.register_echo(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)