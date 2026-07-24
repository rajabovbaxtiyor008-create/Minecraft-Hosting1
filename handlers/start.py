from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import main_menu
from database import add_user

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    add_user(
        message.from_user.id,
        message.from_user.username or "Unknown"
    )

    await message.answer(
        "👋 Добро пожаловать в Minecraft Build Shop!\n\n"
        "Выберите действие в меню ниже.",
        reply_markup=main_menu
    )
