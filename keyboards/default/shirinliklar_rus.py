from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shirinliklar_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Шоколадный торт"),
            KeyboardButton(text="Фруктовый торт")
        ],
        [
            KeyboardButton(text="Ореховый торт"),
            KeyboardButton(text="Наполеон")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)