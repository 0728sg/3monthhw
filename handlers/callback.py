from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import bot, dp

questions = (
    {
        'question': 'which color is better?',
        'options': ['black', 'green', 'blue' ],
        'correct': 0
    },
    {
        'question': 'which car is better?',
        'options': ['bmw', 'mercedes', 'porsche'],
        'correct': 2
    },
    {
        'question': 'what is the best food culture?',
        'options': ['turk', 'france', 'italian'],
        'correct': 0
    }
)


async def start_quiz(message: types.Message):
    await ask_question(message, 0)


async def ask_question(message: types.Message, question_index: int):
    question = questions[question_index]
    keyboard = InlineKeyboardMarkup(row_width=1)
    for i, option in enumerate(question['options']):
        button = InlineKeyboardButton(option, callback_data=f"{question_index}_{i}")
        keyboard.add(button)

    await bot.send_message(message.chat.id, question['question'], reply_markup=keyboard)


async def handle_answer(callback_query: types.CallbackQuery):
    question_index, answer_index = map(int, callback_query.data.split('_'))
    if answer_index == questions[question_index]['correct']:
        await callback_query.message.answer("corerct!")
    else:
        await callback_query.message.answer("uncorrect:(")


    if question_index + 1 < len(questions):
        await ask_question(callback_query.message, question_index + 1)
    else:
        await callback_query.message.answer("quiz is over")

def register_handlers_quiz(dp: Dispatcher):
    dp.register_message_handler(start_quiz, commands=['callback'])
    dp.register_callback_query_handler(handle_answer, lambda c: c.data and '_' in c.data)


register_handlers_quiz(dp)
