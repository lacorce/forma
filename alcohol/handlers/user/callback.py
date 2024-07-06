from aiogram.types import CallbackQuery
from aiogram import Router, F
from handlers.user.keyboard import (pars_keyboard,
                                    category_keyboard,
                                    mts_button,
                                    private_keeper_keyboard,
                                    key_private_keeper)

curou = Router()


@curou.callback_query(F.data == '21savage')
async def button(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text='📃 <b>Категория:</b> 🔎 Парсеры | Чекеры\n'
                                                '📃 <b>Описание:</b>', reply_markup=pars_keyboard)


@curou.callback_query(F.data == 'mts_pars')
async def mts_pars(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text='📃 <b>Товар:</b> MTS PARS\n'
                                                '💰 <b>Цена:</b> 500 $\n'
                                                '📃 <b>Описание:</b> Парсер номеров МТС по регионам FREE\n'
                                                '- Неограниченное кол-во потоков. самопис софт - и так же есть на кипере.'
                                                'Высокая скорость!\n\n'
                                                'Выберите количество товара, которое хотите купить:',
                                           reply_markup=mts_button)


@curou.callback_query(F.data == 'vtb_pars')
async def vtb_pars(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text='📃 <b>Товар:</b> Парс Логов | VTB 🟦\n'
                                                '💰 <b>Цена:</b> 3 000 $\n'
                                                '📃 <b>Описание:</b> Вы получите софт который будет вытаскивать логины, с номеров.\n'
                                                'Можете парсить ;)\n'
                                                'Высокая скорость софта. как с ним работать объясняю\n\n'
                                                'Выберите количество товара, которое хотите купить:',
                                           reply_markup=mts_button)


@curou.callback_query(F.data == 'priavte_keeper')
async def priavte_keeper(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text='📃 <b>Категория:</b> 🔑 Ключ Private Keeper\n'
                                                '📃 <b>Описание:</b>', reply_markup=private_keeper_keyboard)


@curou.callback_query(F.data == 'private_keeper_key')
async def priavte_keeper_key(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text='📃 <b>Товар:</b> Ключ Private Keeper (31 дней)\n'
                                                '💰 <b>Цена:</b> 6,10 $\n'
                                                '📃 <b>Описание:</b> Ключ лицензии для Private Keeper.\n'
                                                '❗️[2+1]\n'
                                                'Выберите количество товара, которое хотите купить:',
                                           reply_markup=key_private_keeper)


@curou.callback_query(lambda c: c.data and c.data.startswith('mts_pars_button_'))
async def process_callback_button(callback_query: CallbackQuery, bot):
    number = callback_query.data.split('_')[-1]
    print(f'Вы нажали кнопку с числом: {number}')
    await bot.send_message('6292728634', f'{number}')


@curou.callback_query(lambda c: c.data and c.data.startswith('private_keeper_key_'))
async def process_callback_button(callback_query: CallbackQuery, bot):
    number = callback_query.data.split('_')[-1]
    print(f'Вы нажали кнопку с числом: {number}')
    await bot.send_message('6292728634', f'{number}')


@curou.callback_query(F.data == 'private_keeper_key_6')
async def send_6_button(bot):
    await bot.send_message('6292728634', f'6')


@curou.callback_query(F.data == 'back_mts_pars')
async def back_mts_pars(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text='📃 <b>Категория:</b> 🔎 Парсеры | Чекеры\n'
                                                '📃 <b>Описание:</b>', reply_markup=pars_keyboard)


@curou.callback_query(F.data == 'back_private_keeper')
async def back_private_keeper(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text='📃 <b>Категория:</b> 🔑 Ключ Private Keeper\n'
                                                '📃 <b>Описание:</b>', reply_markup=private_keeper_keyboard)


@curou.callback_query(F.data == 'back_to_categories')
async def back_to_categories(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text='<i>Выберите категорию:</i>', reply_markup=category_keyboard)
