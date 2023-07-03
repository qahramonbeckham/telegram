from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shirinliklar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Shokoladli tort"),
            KeyboardButton(text="Mevali tort")
        ],
        [
            KeyboardButton(text="Yong'oqli tort"),
            KeyboardButton(text="Napalion")
        ],
        [
            KeyboardButton(text="Orqaga qaytish")
        ]
    ],
    resize_keyboard=True
)