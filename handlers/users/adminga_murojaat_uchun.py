from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states.holatlar import Murojaat
from keyboards.default.adminga_yuborish import adminga_yuborish_buttons
from keyboards.default.menu_uchun import menu_buttons


# Echo bot
@dp.message_handler(text="Adminga murojaat")
async def bot_echo(message: types.Message):
    await message.answer(text="Ismingizni kiriting")
    await Murojaat.ism_qabul_qilish.set()

@dp.message_handler(state=Murojaat.ism_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    ismi = message.text
    await state.update_data({"ism" : ismi})
    await message.answer(text="Familyangizni kiriting")
    await Murojaat.familiya_qabul_qilish.set()

@dp.message_handler(state=Murojaat.familiya_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    familyasi = message.text
    await state.update_data({"familya" : familyasi})
    await message.answer(text="Yoshingizni kiriting")
    await Murojaat.yosh_qabul_qilish.set()

@dp.message_handler(state=Murojaat.yosh_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    yoshi = message.text
    await state.update_data({"yosh" : yoshi})
    await message.answer(text="Telefon raqamingizni kiriting")
    await Murojaat.tel_raqam_qabul_qilish.set()

@dp.message_handler(state=Murojaat.tel_raqam_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    tel_raqami = message.text
    await state.update_data({"tel_raqam" : tel_raqami})
    await message.answer(text="Manzilingizni kiriting")
    await Murojaat.manzil_qabul_qilish.set()

@dp.message_handler(state=Murojaat.manzil_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    manzili = message.text
    await state.update_data({"manzil" : manzili})
    await message.answer(text="Murojaatingizni kiriting")
    await Murojaat.murojaat_qabul_qilish.set()

@dp.message_handler(state=Murojaat.murojaat_qabul_qilish)
async def bot_echo(message: types.Message, state:FSMContext):
    murojaati = message.text
    await state.update_data({"murojaat" : murojaati})

    malumot = await state.get_data()
    ismi = malumot.get("ism")
    familyasi = malumot.get("familya")
    yoshi = malumot.get("yoshi")
    tel_raqami = malumot.get("tel_raqam")
    manzili = malumot.get("manzil")
    murojaat_matni = malumot.get("murojaat")

    ekranga_chiqarish = f"Ism : {ismi} \n"\
                        f"Familya : {familyasi} \n"\
                        f"Yosh : {yoshi} \n"\
                        f"Telefon raqami : {tel_raqami} \n"\
                        f"Manzil : {manzili} \n"\
                        f"Murojaati : {murojaat_matni} \n"

    user_id = message.from_user.id
    await bot.send_message(chat_id=user_id, text=ekranga_chiqarish, reply_markup=adminga_yuborish_buttons)
    await Murojaat.tasdiqlash_holati.set()

@dp.message_handler(state=Murojaat.tasdiqlash_holati, text="Bekor qilish")
async def bot_echo(message: types.Message, state:FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text="Bekor qilindi !!!", reply_markup=menu_buttons)
    await state.finish()

@dp.message_handler(state=Murojaat.tasdiqlash_holati, text="Adminga murojaatni yuborish")
async def bot_echo(message: types.Message, state:FSMContext):
    malumot = await state.get_data()
    ismi = malumot.get("ism")
    familyasi = malumot.get("familya")
    yoshi = malumot.get("yoshi")
    tel_raqami = malumot.get("tel_raqam")
    manzili = malumot.get("manzil")
    murojaat_matni = malumot.get("murojaat")

    ekranga_chiqarish = f"Ism : {ismi} \n" \
                        f"Familya : {familyasi} \n" \
                        f"Yosh : {yoshi} \n" \
                        f"Telefon raqami : {tel_raqami} \n" \
                        f"Manzil : {manzili} \n" \
                        f"Murojaati : {murojaat_matni} \n"
    await bot.send_message(chat_id="134868003", text=ekranga_chiqarish)
    await bot.send_message(chat_id=message.from_user.id, text="Adminga yuborildi")
    await state.finish()



