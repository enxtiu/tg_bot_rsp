LEXICON_RU = {
    '/start': 'Привет!, давай поиграем в игру камень ножницы бумага. Если не знаешь правила воспользуйся командой /help',
    '/help': 'Правила игры: ...',
    'echo': 'ой... я не понимаю тебя((',
    'win': 'Молодец ты выиграл, давай ещё',
    'lose': 'Ты проиграл, хочешь отыграться?)',
    'not_game': "Как захочешь открой клавиатуру и нажми 'давай')"
}

if __name__ == '__main__':
    for k in LEXICON_RU:
        print(LEXICON_RU[k])
