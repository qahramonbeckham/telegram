from aiogram.dispatcher.filters.state import State, StatesGroup

class Murojaat(StatesGroup):
    ism_qabul_qilish = State()
    familiya_qabul_qilish = State()
    yosh_qabul_qilish = State()
    tel_raqam_qabul_qilish = State()
    manzil_qabul_qilish = State()
    murojaat_qabul_qilish = State()
    tasdiqlash_holati = State()