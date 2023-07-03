from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

taomlar_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Плов"),
            KeyboardButton(text="Лагман")
        ],
        [
            KeyboardButton(text="Суп"),
            KeyboardButton(text="Рисовый суп")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)