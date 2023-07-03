from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ichimliklar_buttons = ReplyKeyboardMarkup(
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
            KeyboardButton(text="Orqaga qaytish")
        ]
    ],
    resize_keyboard=True
)