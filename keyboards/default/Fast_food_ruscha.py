from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

fast_food_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Лаваш"),
            KeyboardButton(text="Сендвич")
        ],
        [
            KeyboardButton(text="Гамбургер"),
            KeyboardButton(text="Чизбургер")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)