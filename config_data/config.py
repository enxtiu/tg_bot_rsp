import logging

from dataclasses import dataclass
from logging import getLogger

logging.basicConfig(level=logging.DEBUG, format='#{levelname} {name}: {lineno} - {funcName} - {message}', style='{')

logger = getLogger(__name__)

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot

def load_config() -> Config:

    import os
    from dotenv import load_dotenv, find_dotenv

    load_dotenv(find_dotenv())
    logger.debug("Настройка конфигурации")
    return Config(tg_bot=TgBot(token=os.getenv('TOKEN')))

if __name__ == '__main__':
    pass
