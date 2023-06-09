import asyncio
import datetime
import os

from aiogram import Bot, Dispatcher

from filters import AdminFilter
from config import read_config
from handlers import register_user, register_admin


def register_filters(dp):
    dp.filters_factory.bind(AdminFilter)


def register_handlers(dp):
    register_admin(dp)
    register_user(dp)


async def main():
    config = read_config()

    bot = Bot(token=config.token, parse_mode='HTML')
    dp = Dispatcher(bot)

    register_filters(dp)
    register_handlers(dp)

    bot['config'] = config

    # print(config.admin)

    # if not os.path.exists(f'db\\{DB_NAME}.db'):
    #     create_database()

    print(f'Bot started [{datetime.datetime.now}]')
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
