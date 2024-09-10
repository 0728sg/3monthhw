from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_buttons = KeyboardButton('/start')
mem_buttons = KeyboardButton('/mem')
mem_all_buttons = KeyboardButton('/mem_all')
music_buttons = KeyboardButton('/music')
quiz_buttons = KeyboardButton('/quiz')
game_buttons = KeyboardButton('/game')


start.add(start_buttons, mem_buttons, mem_all_buttons,
          music_buttons)


start_test = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    ).add(
KeyboardButton('/start'),
    KeyboardButton('/mem'),
    KeyboardButton('/mem_all'),
    KeyboardButton('/music'),
    KeyboardButton('/quiz'),
    KeyboardButton('/game')
)

start_test_1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    row_width=2
    )

start_test_1.add(
    KeyboardButton('/start'),
    KeyboardButton('/mem'),
    KeyboardButton('/mem_all'),
    KeyboardButton('/music'),
    KeyboardButton('/quiz'),
    KeyboardButton('/game')
)