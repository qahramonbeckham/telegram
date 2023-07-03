from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

taomlar_ingliz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pilaf"),
            KeyboardButton(text="Lagman")
        ],
        [
            KeyboardButton(text="Soup"),
            KeyboardButton(text="Broth")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)