import datetime
from pathlib import Path
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminStates(StatesGroup):
    in_add_news_mode = State()


async def admin_start(msg: Message):
    name = msg.from_user.full_name
    await msg.answer(f'Hi, admin {name}')


async def add_news(msg: Message):
    await msg.answer(f'Send me your news in text format:')
    await AdminStates.in_add_news_mode.set()


async def add_news_text(msg: Message, state: FSMContext):
    await msg.bot.send_chat_action(msg.from_user.id, 'typing')

    this_file_path = Path(__file__).resolve()
    file_with_news = this_file_path.parents[1] / 'news.txt'

    with open(file_with_news, encoding='utf-8', mode='a') as file:
        file.write(f'{msg.text}')

    await msg.answer(f'News successfully added')
    print(f'Added new news [{datetime.datetime.now()}]')
    await state.finish()


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(add_news, commands=['add'], state=AdminStates.in_add_news_mode, is_admin=True)
