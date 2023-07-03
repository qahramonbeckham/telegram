from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

adminga_yuborish_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Adminga murojaatni yuborish"),
            KeyboardButton(text="Bekor qilish")
        ],

    ],
    resize_keyboard=True
)