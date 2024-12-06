from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


def creat_keyboard(
        *buttons: str,
        placehoder: str | bool = False,
        one_time_key: bool = False,
        resize_key: bool = False,
        size: tuple[int, ...] = (2,)
):
    keyboard = ReplyKeyboardBuilder()
    for item in buttons:
        keyboard.add(KeyboardButton(text=item))

    return keyboard.adjust(*size).as_markup(
        resize_keyboard=resize_key,
        one_time_keyboard=one_time_key,
        input_field_placeholder=placehoder
    )


if __name__ == '__main__':
    print(creat_keyboard('122','12'))
