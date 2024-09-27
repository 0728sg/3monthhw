import sqlite3
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3.1')
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


async def start_sending_products(message: types.Message):
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)

    show_all_products = InlineKeyboardButton(text="Look",
                                             callback_data="show_all")
    keyboard.add(show_all_products)

    await message.answer(text='Put on button to look on products:',
                         reply_markup=keyboard)


async def send_all_products(callback_query: types.CallbackQuery):
    products = fetch_all_products()

    if products:
        for product in products:
            caption = (f"Article - {product['product_id']}\n"
                       f"Product name - {product['name_product']}\n"
                       f"Information about product - {product['info_product']}\n"
                       f"Categpry - {product['category']}\n"
                       f"Size - {product['size']}\n"
                       f"Price - {product['price']} сом\n")
            await callback_query.message.answer_photo(photo=product['photo'],
                                                      caption=caption)
    else:
        await callback_query.message.answer("Products not found")


def register_send_products_handler(dp: Dispatcher):
    dp.register_message_handler(start_sending_products, commands=['send_products'])
    dp.register_callback_query_handler(send_all_products, Text(equals='show_all'))
