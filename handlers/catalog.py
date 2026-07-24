from aiogram import Router, F
from aiogram.types import Message

from keyboards import buy_button
from database import get_builds

router = Router()


@router.message(F.text == "📦 Каталог")
async def catalog(message: Message):
    builds = get_builds()

    if not builds:
        await message.answer("📦 Пока нет доступных сборок.")
        return

    for build in builds:
        build_id = build[0]
        name = build[1]
        description = build[2]
        price = build[3]

        text = (
            f"📦 <b>{name}</b>\n\n"
            f"{description}\n\n"
            f"💰 Цена: {price} ₽"
        )

        await message.answer(
            text,
            reply_markup=buy_button(build_id)
        )
