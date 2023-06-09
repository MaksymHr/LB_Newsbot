import typing

from aiogram.dispatcher.filters import BoundFilter

from lb13.config import Config


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj):
        if self.is_admin is None:
            return False

        config: Config = obj.bot.get('config')

        return (obj.from_user.id == config.admin) == self.is_admin
