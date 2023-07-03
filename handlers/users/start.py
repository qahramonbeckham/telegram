from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_uchun import menu_buttons
from loader import dp, bot
from keyboards.default.taomlar_uchun import taomlar_buttons
from keyboards.default.Ichimliklar_uchun import ichimliklar_buttons
from keyboards.default.Shirinliklar_uchun import shirinliklar_buttons
from keyboards.default.Fast_food import fast_food_buttons
from keyboards.inline.tillar_uchun import tillar_buttons
from aiogram.types import CallbackQuery, InputFile
from keyboards.default.menu_ruscha import menu_rus
from keyboards.default.Ichimliklar_ruscha import ichimliklar_rus
from keyboards.default.Taomlar_ruscha import taomlar_rus
from keyboards.default.menu_inglizcha import menu_ingliz
from keyboards.default.shirinliklar_rus import shirinliklar_rus
from keyboards.default.Fast_food_ruscha import fast_food_rus
from keyboards.default.taomlar_inglizcha import taomlar_ingliz
from keyboards.default.ichimliklar_inglizcha import ichimliklar_ingliz
from keyboards.default.shirinliklar_inglizcha import shirinliklar_ingliz
from keyboards.default.fast_food_inglizcha import fast_food_ingliz
from filters import Shaxsiy


@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=tillar_buttons)

@dp.callback_query_handler(text="til1")
async def bot_start(message: CallbackQuery):
    await message.message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_buttons)

@dp.callback_query_handler(text="til2")
async def bot_start(message: CallbackQuery):
    await message.message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=menu_rus)

@dp.callback_query_handler(text="til3")
async def bot_start(message: CallbackQuery):
    await message.message.answer(f"Hello, {message.from_user.full_name}!", reply_markup=menu_ingliz)

# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_buttons)

@dp.message_handler(text="Taomlar")
async def bot_start(message: types.Message):
    await message.answer(f"Taomlar", reply_markup=taomlar_buttons)

@dp.message_handler(text="Ichimliklar")
async def bot_start(message: types.Message):
    await message.answer(f"Ichimliklar", reply_markup=ichimliklar_buttons)

@dp.message_handler(text="Shirinliklar")
async def bot_start(message: types.Message):
    await message.answer(f"Shirinliklar", reply_markup=shirinliklar_buttons)

@dp.message_handler(text="Fast food")
async def bot_start(message: types.Message):
    await message.answer(f"Fast food", reply_markup=fast_food_buttons)

@dp.message_handler(text="Orqaga qaytish")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, menuga hush kelibsiz!", reply_markup=menu_buttons)

@dp.message_handler(text="Еда")
async def bot_start(message: types.Message):
    await message.answer(f" Еда", reply_markup=taomlar_rus)

@dp.message_handler(text="Напитки")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, botga hush kelibsiz!", reply_markup=ichimliklar_rus)

@dp.message_handler(text="Сладости")
async def bot_start(message: types.Message):
    await message.answer(f"Сладости", reply_markup=shirinliklar_rus)

@dp.message_handler(text="Назад")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, botga hush kelibsiz!", reply_markup=menu_rus)

@dp.message_handler(text="Фаст фуд")
async def bot_start(message: types.Message):
    await message.answer(f"Fast food", reply_markup=fast_food_rus)

@dp.message_handler(text="Foods")
async def bot_start(message: types.Message):
    await message.answer(f"Foods", reply_markup=taomlar_ingliz)

@dp.message_handler(text="Drinks")
async def bot_start(message: types.Message):
    await message.answer(f"Drinks", reply_markup=ichimliklar_ingliz)

@dp.message_handler(text="Sweets")
async def bot_start(message: types.Message):
    await message.answer(f"Sweets", reply_markup=shirinliklar_ingliz)

@dp.message_handler(text="Fast foods")
async def bot_start(message: types.Message):
    await message.answer(f"Fast foods", reply_markup=fast_food_ingliz)

@dp.message_handler(text="Back")
async def bot_start(message: types.Message):
    await message.answer(f"welcome in menu", reply_markup=menu_ingliz)

@dp.message_handler(text="Osh")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/11"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Osh ---\n"
                         "Narhi: --- 30 000 ---")

@dp.message_handler(text="Lag'mon")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/5"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Lag'mon ---\n"
                         "Narhi: --- 25 000 ---")

@dp.message_handler(text="Mastava")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/7"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Mastava ---\n"
                         "Narhi: --- 20 000 ---")

@dp.message_handler(text="Sho'rva")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Sho'rva ---\n"
                         "Narhi: --- 23 000 ---")

@dp.message_handler(text="Pepsi")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/12"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Pepsi ---\n"
                         "Narhi: --- 12 000 ---")

@dp.message_handler(text="Fanta")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Fanta ---\n"
                         "Narhi: --- 12 000 ---")

@dp.message_handler(text="Sprite")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/16"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Sprite ---\n"
                         "Narhi: --- 11 000 ---")

@dp.message_handler(text="Montella")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Montella ---\n"
                         "Narhi: --- 6 000 ---")

@dp.message_handler(text="Shokoladli tort")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/15"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Shokoladli tort ---\n"
                         "Narhi: --- 15 000 ---")

@dp.message_handler(text="Mevali tort")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/8"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Mevali tort ---\n"
                         "Narhi: --- 14 000 ---")

@dp.message_handler(text="Yong'oqli tort")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/17"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Yong'oqli tort ---\n"
                         "Narhi: --- 12 000 ---")

@dp.message_handler(text="Napaleon")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/10"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Napaleon ---\n"
                         "Narhi: --- 10 000 ---")

@dp.message_handler(text="Lavash")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/6"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Lavash ---\n"
                         "Narhi: --- 22 000 ---")

@dp.message_handler(text="Sendvich")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/13"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Sendvich ---\n"
                         "Narhi: --- 24 000 ---")

@dp.message_handler(text="Chizburger")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/2"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Chizburger ---\n"
                         "Narhi: --- 27 000 ---")

@dp.message_handler(text="Gamburger")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/4"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Nomi: --- Gamburger ---\n"
                         "Narhi: --- 21 000 ---")

@dp.message_handler(text="Плов")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/11"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Плов ---\n"
                         "Цена: --- 30 000 ---")

@dp.message_handler(text="Лагман")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/5"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Лагман ---\n"
                         "Цена: --- 25 000 ---")

@dp.message_handler(text="Рисовый суп")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/7"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Рисовый суп ---\n"
                         "Цена: --- 20 000 ---")

@dp.message_handler(text="Суп")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Суп ---\n"
                         "Цена: --- 23 000 ---")

@dp.message_handler(text="Пепси")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/12"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Пепси ---\n"
                         "Цена: --- 12 000 ---")

@dp.message_handler(text="Фанта")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Фанта ---\n"
                         "Цена: --- 12 000 ---")

@dp.message_handler(text="Спрайт")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/16"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Спрайт ---\n"
                         "Цена: --- 11 000 ---")

@dp.message_handler(text="Монтелла")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Монтелла ---\n"
                         "Цена: --- 6 000 ---")

@dp.message_handler(text="Шоколадный торт")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/15"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Шоколадный торт ---\n"
                         "Цена: --- 15 000 ---")

@dp.message_handler(text="Фруктовый торт")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/8"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Фруктовый торт ---\n"
                         "Цена: --- 14 000 ---")

@dp.message_handler(text="Ореховый торт")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/17"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Ореховый торт ---\n"
                         "Цена: --- 12 000 ---")

@dp.message_handler(text="Наполеон")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/10"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Наполеон ---\n"
                         "Цена: --- 10 000 ---")

@dp.message_handler(text="Лаваш")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/6"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Лаваш ---\n"
                         "Цена: --- 22 000 ---")

@dp.message_handler(text="Сендвич")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/13"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Сендвич ---\n"
                         "Цена: --- 24 000 ---")

@dp.message_handler(text="Чизбургер")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/2"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Чизбургер ---\n"
                         "Цена: --- 27 000 ---")

@dp.message_handler(text="Гамбургер")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/4"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Названия: --- Гамбургер ---\n"
                         "Цена: --- 21 000 ---")

@dp.message_handler(text="Pilaf")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/11"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Pilaf ---\n"
                         "Price: --- 30 000 ---")

@dp.message_handler(text="Lagman")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/5"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Lagman ---\n"
                         "Price: --- 25 000 ---")

@dp.message_handler(text="Broth")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/7"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Broth ---\n"
                         "Price: --- 20 000 ---")

@dp.message_handler(text="Soup")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/14"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Soup ---\n"
                         "Price: --- 23 000 ---")

@dp.message_handler(text="Pepsi")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/12"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Pepsi ---\n"
                         "Price: --- 12 000 ---")

@dp.message_handler(text="Fanta")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/3"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Fanta ---\n"
                         "Price: --- 12 000 ---")

@dp.message_handler(text="Sprite")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/16"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Sprite ---\n"
                         "Price: --- 11 000 ---")

@dp.message_handler(text="Montella")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/9"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Montella ---\n"
                         "Price: --- 6 000 ---")

@dp.message_handler(text="Chocolate cake")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/15"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Chocolate cake ---\n"
                         "Price: --- 15 000 ---")

@dp.message_handler(text="Fruit cake")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/8"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Fruit cake ---\n"
                         "Price: --- 14 000 ---")

@dp.message_handler(text="Walnut cake")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/17"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Walnut cake ---\n"
                         "Price: --- 12 000 ---")

@dp.message_handler(text="Napaleon")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/10"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Napaleon ---\n"
                         "Price: --- 10 000 ---")

@dp.message_handler(text="Lavash")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/6"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Lavash ---\n"
                         "Price: --- 22 000 ---")

@dp.message_handler(text="Sendvich")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/13"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Sendvich ---\n"
                         "Price: --- 24 000 ---")

@dp.message_handler(text="Chizburger")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/2"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Chizburger ---\n"
                         "Price: --- 27 000 ---")

@dp.message_handler(text="Gamburger")
async def bot_start(message: types.Message):
    osh_manzili = "https://t.me/rasmlar1988/4"
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id, photo=osh_manzili, caption="Name: --- Gamburger ---\n"
                         "Price: --- 21 000 ---")

@dp.message_handler(commands="Boshlash")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, botga hush kelibsiz!")


@dp.message_handler(text="Salom")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, botga hush kelibsiz!")
