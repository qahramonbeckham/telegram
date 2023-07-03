from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Еда"),
            KeyboardButton(text="Напитки")
        ],
        [
            KeyboardButton(text="Сладости"),
            KeyboardButton(text="Фаст фуд")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)