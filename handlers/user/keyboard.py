from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup)

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📖Все категории📖'),
            KeyboardButton(text='📑Наличие товаров📑')
        ],
        [
            KeyboardButton(text='💡О магазине'),
            KeyboardButton(text='👤Профиль👤')
        ],
        [
            KeyboardButton(text='📌 ЧАТ 📌')
        ],
        [
            KeyboardButton(text='⚠️ СЛУЖБА ПОДДЕРЖКИ ⚠️')
        ]
    ], resize_keyboard=True
)
# async def create_category_keyboard():
# for u :3
#    products = await database()
#    keyboard = InlineKeyboardMarkup()
#    for product in products:
#        button = InlineKeyboardButton(text=product[1], callback_data=f'product_{product[0]}')
#        keyboard.add(button)
category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔎 Парсеры | Чекеры', callback_data='21savage')
        ],
        [
            InlineKeyboardButton(text='🔑 Ключ Private Keeper', callback_data='priavte_keeper')
        ]
    ]
)
pars_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='MTS PARS | 500$ | ∞ ', callback_data='mts_pars')
        ],
        [
            InlineKeyboardButton(text='Парс Логов | VTB🟦| 3 000$ | ∞', callback_data='vtb_pars')
        ],
        [
            InlineKeyboardButton(text='🤍', callback_data='heart')
        ],
        [
            InlineKeyboardButton(text='Назад ко всем категориям', callback_data='back_to_categories')
        ]
    ]
)
mts_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f'{i}', callback_data=f'mts_pars_button_{i}')
            for i in range(1, 6)
        ],
        [
            InlineKeyboardButton(text=f'{i}', callback_data=f'mts_pars_button_{i}')
            for i in range(6, 11)
        ],
        [
            InlineKeyboardButton(text='Ввести свое кол-во', callback_data='other_sum')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_mts_pars'),
            InlineKeyboardButton(text='Назад ко всем категориям', callback_data='back_to_categories')
        ]
    ]
)

private_keeper_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ключ Private Keeper (31 дней) | 6,10 $ ❗ [2+1] | 6 шт.',
                                 callback_data='private_keeper_key')
        ],
        [
            InlineKeyboardButton(text='🤍', callback_data='heart')
        ],
        [
            InlineKeyboardButton(text='Назад ко всем категориям', callback_data='back_to_categories')
        ]
    ]
)

key_private_keeper = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=f'{i}', callback_data=f'private_keeper_key_{i}')
            for i in range(1, 6)
        ],
        [
            InlineKeyboardButton(text=f'6', callback_data=f'private_keeper_key_6')
        ],
        [
            InlineKeyboardButton(text='Ввести свое кол-во', callback_data='other_sum')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back_private_keeper'),
            InlineKeyboardButton(text='Назад ко всем категориям', callback_data='back_to_categories')
        ]
    ]
)
