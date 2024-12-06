import asyncio
import logging

from aiogram import Bot, Dispatcher, Router

from config_data.config import Config, load_config

logging.basicConfig(level=logging.DEBUG, format='#{levelname} {name}: {lineno} - {funcName} - {message}', style='{')

logger = logging.getLogger(__name__)

async def main() -> None:

    config: Config = load_config()

    logger.debug("Init bot, dp")
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    logger.debug("start polling")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
