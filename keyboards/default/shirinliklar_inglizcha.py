from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shirinliklar_ingliz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Chocolate cake"),
            KeyboardButton(text="Fruit cake")
        ],
        [
            KeyboardButton(text="Walnut cake"),
            KeyboardButton(text="Napaleon")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)