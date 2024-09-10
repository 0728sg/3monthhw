from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import bot, dp


async def game(message: types.Message):
    games = ['football', 'casino', 'basketball', 'pulyalka', 'bowling', 'kosti']
    await bot.send_dice(message.chat.id, emoji=games)


async def echo(message: types.Message):
    if "game" in message.text.lower():
        bot_dice = await bot.send_dice(message.chat.id, emoji='kosti')
        player_dice = await bot.send_dice(message.chat.id, emoji='kosti')

        bot_value = bot_dice.dice.value
        player_value = player_dice.dice.value

        if bot_value > player_value:
            await bot.send_message(message.chat.id, f"bot win (Бот: {bot_value}, Вы: {player_value})")
        elif bot_value < player_value:
            await bot.send_message(message.chat.id, f"you win (Бот: {bot_value}, Вы: {player_value})")
        else:
            await bot.send_message(message.chat.id, f"nichya (Бот: {bot_value}, Вы: {player_value})")
    else:
        try:
            number = float(message.text)
            result = number ** 2
            await message.answer(f'square: {result}')
        except ValueError:
            await message.answer(message.text)


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
    dp.register_message_handler(echo)