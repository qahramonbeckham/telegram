from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ichimliklar_ingliz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Fanta")
        ],
        [
            KeyboardButton(text="Sprite"),
            KeyboardButton(text="Montella")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)