from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from config import ADMIN_IDS

router = Router()


class AddBuild(StatesGroup):
    name = State()
    description = State()
    price = State()


@router.message(Command("admin"))
async def admin_panel(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        return

    await message.answer(
        "👑 Админ-панель\n\n"
        "/addbuild - Добавить сборку"
    )


@router.message(Command("addbuild"))
async def add_build(message: Message, state: FSMContext):
    if message.from_user.id not in ADMIN_IDS:
        return

    await state.set_state(AddBuild.name)
    await message.answer("📦 Введите название сборки:")

@router.message(AddBuild.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddBuild.description)

    await message.answer("📝 Введите описание сборки:")


@router.message(AddBuild.description)
async def get_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(AddBuild.price)

    await message.answer("💰 Введите цену:")

from database import add_build

@router.message(AddBuild.price)
async def get_price(message: Message, state: FSMContext):
    try:
        price = float(message.text)
    except ValueError:
        await message.answer("❌ Введите цену числом.")
        return

    data = await state.get_data()

    add_build(
        name=data["name"],
        description=data["description"],
        price=price,
        file="",
        photo=""
    )

    await state.clear()

    await message.answer(
        "✅ Сборка успешно добавлена!\n\n"
        f"📦 {data['name']}\n"
        f"💰 Цена: {price} ₽"
    )
