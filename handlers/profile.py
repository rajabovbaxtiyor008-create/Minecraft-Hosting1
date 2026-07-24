from aiogram import Router, F
from aiogram.types import Message
import sqlite3

router = Router()


@router.message(F.text == "👤 Профиль")
async def profile(message: Message):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT balance FROM users WHERE telegram_id=?",
        (message.from_user.id,)
    )

    user = cur.fetchone()

    if user:
        balance = user[0]
    else:
        balance = 0

    conn.close()

    await message.answer(
        f"""👤 <b>Ваш профиль</b>

🆔 ID: <code>{message.from_user.id}</code>
💰 Баланс: {balance} ₽
📦 Покупок: скоро будет
"""
    )
