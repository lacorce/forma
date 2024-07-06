from aiogram import Bot, Dispatcher
import asyncio
from handlers.user.callback import curou
from aiogram.types import Message
from aiogram.filters import CommandStart
from handlers.user.keyboard import start_keyboard
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.user.message import murou, commands

dp = Dispatcher()
bot = Bot(token='7490494153:AAE-XIhKK5TZfwWbHndmvRSt_HYkU5FD-rg',
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('🏘 Меню')
    await message.answer(f'my Приветствуем тебя {message.from_user.first_name} в пиз**том боте\n'
                         '- У нас есть все для ворка, и мы расширяемся 😎', reply_markup=start_keyboard)


async def run_bot():
    dp.include_router(murou)
    dp.include_router(curou)
    await commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(run_bot())
