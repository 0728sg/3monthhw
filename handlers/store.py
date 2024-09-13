from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from db import db_main
import buttons
from aiogram.types import ReplyKeyboardRemove



class FSM_Store(StatesGroup):
    id = State()
    name_products = State()
    size = State()
    price = State()
    product_id = State()
    category = State()
    info_product = State()
    photo_products = State()
    submit = State()


async def start_fsm(message: types.Message):
    await message.answer('write product name: ', reply_markup=buttons.cancel_button)
    await FSM_Store.name_products.set()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_products'] = message.text

    await message.answer('write size: ')
    await FSM_Store.next()


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('write category: ')
    await FSM_Store.next()


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer('write a price: ')
    await FSM_Store.next()


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer('write an article): ')
    await FSM_Store.next()


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('send photo: ')
    await FSM_Store.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer('is data correct?')
    await message.answer_photo(
        photo=data['photo'],
        caption=f'product name: {data["name_products"]}\n'
                f'size: {data["size"]}\n'
                f'category: {data["category"]}\n'
                f'price: {data["price"]}\n'
                f'article: {data["product_id"]}\n',
        reply_markup=buttons.submit_button)

    await FSM_Store.next()


async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'yes':
        async with state.proxy() as data:
          await message.answer('data is on the base', reply_markup=kb)
          await db_main.sql_insert_products(
              id=data['id'],
              name_products=data['name_products'],
              size=data['size'],
              price=data['price'],
              product_id=data['product_id'],
              category=data['category'],
              indo_product=data['indo_product'],
              photo_products=data['photo_products'],
          )
          await state.finish()

    elif message.text == 'no':
        await message.answer('you finished', reply_markup=kb)
        await state.finish()

    else:
        await message.answer('Choose "yes" или "no"')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    kb = ReplyKeyboardRemove()
    if current_state is not None:
        await state.finish()
        await message.answer('canceled', reply_markup=kb)



def register_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(start_fsm, commands=['store'])
    dp.register_message_handler(load_name, state=FSM_Store.name_products)
    dp.register_message_handler(load_size, state=FSM_Store.size)
    dp.register_message_handler(load_category, state=FSM_Store.category)
    dp.register_message_handler(load_price, state=FSM_Store.price)
    dp.register_message_handler(load_product_id, state=FSM_Store.product_id)
    dp.register_message_handler(load_photo, state=FSM_Store.photo_products, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_Store.submit)
