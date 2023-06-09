from dataclasses import dataclass

from environs import Env


@dataclass
class Config:
    token: str
    admin: list[int]


def read_config(path='.env'):
    env = Env()
    env.read_env(path)

    return Config(
        token=env.str('TOKEN'),
        admin=env.int('ADMIN'),
    )
