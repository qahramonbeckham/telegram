from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

fast_food_buttons = ReplyKeyboardMarkup(
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
            KeyboardButton(text="Orqaga qaytish")
        ]
    ],
    resize_keyboard=True
)