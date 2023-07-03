from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ichimliklar_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пепси"),
            KeyboardButton(text="Фанта")
        ],
        [
            KeyboardButton(text="Спрайт"),
            KeyboardButton(text="Монтелла")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)