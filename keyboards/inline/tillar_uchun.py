from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tillar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili", callback_data="til1"),
            InlineKeyboardButton(text="Rus tili", callback_data="til2")
        ],
        [
            InlineKeyboardButton(text="ingliz tili", callback_data="til3")
        ]
    ]
)