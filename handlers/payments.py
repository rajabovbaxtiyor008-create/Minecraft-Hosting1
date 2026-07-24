from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith("buy_"))
async def buy_build(callback: CallbackQuery):
    build_id = callback.data.split("_")[1]

    await callback.message.answer(
        f"💳 Вы выбрали сборку №{build_id}\n\n"
        "⚠️ Оплата пока не подключена."
    )

    await callback.answer()
