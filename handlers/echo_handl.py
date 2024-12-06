from aiogram import Router, types

from keyboards.keyboard import creat_keyboard
from lexicon_data.lexicon import LEXICON_RU

router: Router = Router()

start_game = creat_keyboard(
        'Давай', 'Не хочу',
        placehoder='Смотри кнопки снизу',
        one_time_key=True,
        resize_key=True
    )


@router.message()
async def get_echo(message: types.Message) -> None:
    await message.answer(LEXICON_RU['echo'], reply_markup=start_game)

if __name__ == '__main__':
    pass
