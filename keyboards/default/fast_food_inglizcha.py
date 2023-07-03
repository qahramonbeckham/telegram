from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

fast_food_ingliz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lavash"),
            KeyboardButton(text="Sendvich")
        ],
        [
            KeyboardButton(text="Chizburger"),
            KeyboardButton(text="Gamburger")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)