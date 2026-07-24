from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMIN_IDS

router = Router()


@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.answer("❌ У вас нет доступа.")
        return

    text = (
        "👑 <b>Админ-панель</b>\n\n"
        "1. /addbuild - Добавить сборку\n"
        "2. /listbuilds - Список сборок\n"
        "3. /stats - Статистика\n"
        "4. /broadcast - Рассылка"
    )

    await message.answer(text)


@router.message(Command("stats"))
async def stats(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        return

    import sqlite3

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users")
    users = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM builds")
    builds = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM purchases")
    purchases = cur.fetchone()[0]

    conn.close()

    await message.answer(
        f"📊 Статистика\n\n"
        f"👤 Пользователей: {users}\n"
        f"📦 Сборок: {builds}\n"
        f"🛒 Покупок: {purchases}"
    )
