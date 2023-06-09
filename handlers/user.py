import random
from pathlib import Path

from aiogram import Dispatcher
from aiogram.types import Message


async def start_user(msg: Message):
    name = msg.from_user.first_name
    await msg.answer(f"Hi, {name}. I'm a news bot. Send /get_news to getting news!")


async def send_news(msg: Message):
    await msg.bot.send_chat_action(msg.from_user.id, 'typing')

    this_file_path = Path(__file__).resolve()
    file_with_news = this_file_path.parents[1] / 'news.txt'

    with open(file_with_news, encoding='utf-8') as file:
        news = file.readlines()

    if not news:
        await msg.answer('Sorry, we don\'t have news yet.')
    else:
        news = list(a.rstrip('\n') for a in news)
        await msg.answer(f'{random.choice(news)}\n\n'
                         f'Have a great day!')


async def status(msg: Message):
    this_file_path = Path(__file__).resolve()
    file_with_news = this_file_path.parents[1] / 'news.txt'

    with open(file_with_news, encoding='utf-8') as f:
        news = f.readlines()
        news_count = len(news)
        del news

    await msg.answer(f'Hi. In our library {news_count} news at this moment!')


def register_user(dp: Dispatcher):
    dp.register_message_handler(start_user, commands=["start"], state="*")
    dp.register_message_handler(send_news, commands=['get_news'], state='*')
    dp.register_message_handler(status, commands=['status'], state='*')
