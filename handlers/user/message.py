from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.user.keyboard import category_keyboard
from aiogram.types import BotCommand, BotCommandScopeDefault


class help(StatesGroup):
    handling = State()


murou = Router()


async def commands(bot):
    commands = [BotCommand(command='start', description='Main menu'),
                BotCommand(command='catalog', description='categories'),
                BotCommand(command='help', description='Help')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


@murou.message(F.text == '📖Все категории📖')
async def categories(message: Message):
    await message.answer('<i>Выберите категорию:</i>', reply_markup=category_keyboard)


@murou.message(Command('catalog'))
async def catalog(message: Message):
    await message.answer(f'<i>Выберите категорию:</i>', reply_markup=category_keyboard)


@murou.message(F.text == '📑Наличие товаров📑')
async def products(message: Message):
    await message.answer(f'data from the database')


@murou.message(F.text == '💡О магазине')
async def ab_store(message: Message):
    await message.answer(f'<b>🏠Магазин :</b>unamestore\n'
                         f'⏰ <b>Дата создания:</b>udata\n'
                         f'💬 <b>Чат:</b>ulink\n'
                         f'📢 <b>Канал:</b>ulink')


@murou.message(F.text == '👤Профиль👤')
async def profile(message: Message):
    await message.answer(f'👤 Имя: {message.from_user.first_name}\n'
                         f'🔑 ID: {message.from_user.id}\n'
                         f'⏱ Регистрация: connect with database\n\n'
                         f'💰 Ваш баланс: connect with database\n\n'
                         f'connect with database - Количество заказов\n\n'
                         f'<tg-spoiler><b>connect with database</b></tg-spoiler> - Сумма заказов')


@murou.message(F.text == '📌 ЧАТ 📌')
async def chat(message: Message):
    await message.answer('Наш чат: ulink')


@murou.message(Command('help'))
async def button_help(message: Message):
    await message.answer('По всем вопросам писать: @urtgfirstname')


@murou.message(F.text == '⚠️ СЛУЖБА ПОДДЕРЖКИ ⚠️')
async def support(message: Message, state: FSMContext):
    await state.set_state(help.handling)
    await message.answer('Опишите свой вопрос или проблему:')


@murou.message(help.handling)
async def support_handling(message: Message, state: FSMContext):
    await state.update_data(handling=message.text)
    data = await state.get_data()
    await state.clear()
    print(data['handling'])
