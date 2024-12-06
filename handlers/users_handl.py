import logging, random

from aiogram import filters, types, Router, F
from aiogram.filters import Command

from keyboards.keyboard import creat_keyboard
from lexicon_data.lexicon import LEXICON_RU

logging.basicConfig(level=logging.DEBUG, format='#{levelname} {name}: {lineno} - {funcName} - {message}', style='{')
logger = logging.getLogger(__name__)

router = Router()

start_game = creat_keyboard(
        'Давай', 'Не хочу',
        placehoder='Смотри кнопки снизу',
        one_time_key=True,
        resize_key=True
    )

choice_user = creat_keyboard(
        'Ножницы', 'Бумага', 'Камень',
        placehoder='Смотри кнопки снизу',
        one_time_key=True,
        resize_key=True
    )
choice_list = ['Ножницы', 'Бумага', 'Камень']

class ChoiceFilter(filters.BaseFilter):

    async def __call__(self, message: types.Message) -> bool | dict[str, str]:
        if message.text not in choice_list:
            return False
        else:
            return {'key_' + str(i):choice_list[i] for i in range(3)}

@router.message(filters.CommandStart())
async def get_start(message: types.Message) -> None:
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_game)

@router.message(Command(commands='help'))
async def get_help(message: types.Message) -> None:
    await message.answer(text=LEXICON_RU['/help'], reply_markup=start_game)

@router.message(F.text == 'Давай')
async def get_go(message: types.Message) -> None:
    await message.answer(text='Выбирай)', reply_markup=choice_user)

@router.message(F.text == 'Не хочу')
async def get_not_game(message: types.Message) -> None:
    await message.answer(text=LEXICON_RU['not_game'], reply_markup=start_game)

@router.message(ChoiceFilter())
async def get_choice(message: types.Message, key_0: str, key_1: str, key_2: str) -> None:

    def random_choice() -> str: return choice_list[random.randrange(0, 3)]

    choice = random_choice()

    if message.text == choice:
        await message.answer(text='У меня тоже) ещё попытка', reply_markup=creat_keyboard(
        key_0, key_1, key_2,
        placehoder='Смотри кнопки снизу',
        one_time_key=True,
        resize_key=True
    ))
    else:
        if message.text == key_1 and choice == key_2:
            await get_win(message)
        elif message.text == key_1:
            await get_lose(message)

        if message.text == key_0 and choice == key_1:
            await get_win(message)
        elif message.text == key_0:
            await get_lose(message)

        if message.text == key_2 and choice == key_0:
            await get_win(message)
        elif message.text == key_2:
            await get_lose(message)


async def get_win(message: types.Message) -> None:
    await message.answer(
        text=LEXICON_RU['win'],
        reply_markup=start_game,
        )

async def get_lose(message: types.Message) -> None:
    await message.answer(
        text=LEXICON_RU['lose'],
        reply_markup=start_game,
        )

if __name__ == '__main__':
    pass
