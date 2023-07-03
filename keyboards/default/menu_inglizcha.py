from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_ingliz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foods"),
            KeyboardButton(text="Drinks")
        ],
        [
            KeyboardButton(text="Sweets"),
            KeyboardButton(text="Fast foods")
        ],
        [
            KeyboardButton(text="Back")
        ]
    ],
    resize_keyboard=True
)