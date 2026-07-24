from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Каталог")],
        [KeyboardButton(text="🛒 Мои покупки"),
         KeyboardButton(text="👤 Профиль")],
        [KeyboardButton(text="📞 Поддержка")]
    ],
    resize_keyboard=True
)


# Кнопка "Назад"
back_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)


# Кнопка покупки
def buy_button(build_id: int):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🛒 Купить",
                callback_data=f"buy_{build_id}"
            )]
        ]
    )
