from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio

from config import BOT_TOKEN
from database import create_tables

# Импорт роутеров
from handlers.start import router as start_router
from handlers.catalog import router as catalog_router
from handlers.profile import router as profile_router
from handlers.admin import router as admin_router
from handlers.payments import router as payments_router


async def main():
    # Создаем таблицы БД
    create_tables()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(catalog_router)
    dp.include_router(profile_router)
    dp.include_router(admin_router)
    dp.include_router(payments_router)

    print("✅ Бот запущен!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
