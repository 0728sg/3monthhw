import sqlite3
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.dispatcher.filters import Text


def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM products p 
    INNER JOIN products_details pd ON p.product_id = pd.product_id  
    """).fetchall()
    conn.close()
    return products


def delete_product(product_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM products WHERE product_id + ?", (product_id,))
    conn.commit()
    conn.close()
async def is_admin(user_id: int, chat_id: int, bot) -> bool:
    member = await bot.get_chat_member(chat_id, user_id)
    return member.is_chat_admin()


async def start_sending_products(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    show_all_products = InlineKeyboardButton(text="Look",
                                             callback_data="show_all")
    keyboard.add(show_all_products)

    await message.answer(text='put on button to look on products:',
                         reply_markup=keyboard)


async def send_all_products(callback_query: types.CallbackQuery):
    products = fetch_all_products()

    if products:
        for product in products:
            caption = (f"article - {product['product_id']}\n"
                       f"Product name - {product['name_product']}\n"
                       f"Information about product - {product['info_product']}\n"
                       f"Category - {product['category']}\n"
                       f"Size - {product['size']}\n"
                       f"Price - {product['price']} сом\n")

            keyboard = InlineKeyboardMarkup()
            delete_button = InlineKeyboardButton(
                text="Delete product", callback_data=f"delete_{product['product_id']}"
            )
            keyboard.add(delete_button)

            await callback_query.message.answer_photo(photo=product['photo'], caption=caption, reply_markup=keyboard)
    else:
        await callback_query.message.answer("Products not found")


async def delete_product_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    chat_id = callback_query.message.chat.id
    bot = callback_query.bot

    if await is_admin(user_id, chat_id, bot):
        product_id = callback_query.data.split('_')
        delete_product(product_id)

        await callback_query.message.answer(f"product with article {product_id} successfully deleted.")
        if callback_query.message.photo:
            new_caption = 'Product deleted. \n Update ur list'

            photo_404 = open('/media/img.png', 'rb')

        await callback_query.message.edit_media(
            InputMediaPhoto(media=photo_404,
                            caption=new_caption))

    else:
        await callback_query.message.answer(
            "You dont have rights to delete this product")



def register_send_products_delete_handler(dp: Dispatcher):
    dp.register_message_handler(start_sending_products, commands=['products'])
    dp.register_callback_query_handler(send_all_products, Text(equals='show_all_delete'))
    dp.register_callback_query_handler(delete_product_handler, Text(startswith='delete'))
