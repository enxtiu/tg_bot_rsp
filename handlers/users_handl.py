import logging

from aiogram import filters, types, F, Router
from aiogram.filters import CommandStart

logging.basicConfig(level=logging.DEBUG, format='#{levelname} {name}: {lineno} - {funcName} - {message}', style='{')
logger = logging.getLogger(__name__)

router = Router()

@router.message(filters.CommandStart)
async def get_start(message: types.Message) -> None:
    pass

if __name__ == '__main__':
    pass
