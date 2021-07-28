from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=False):
    """
    Возвращает случайные шутки из 3х списков

    :param n: колличество шуток
    :param repeat: проверка на уникальность
    :return: список шуток

    """
    nou, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes_list = []
    min_list = min(nou, adv, adj)

    while n and len(min_list):
        num = randrange(len(min_list))
        if repeat:
            jokes_list.append(f'{nou.pop(num)} {adv.pop(num)} {adj.pop(num)}')
        else:
            jokes_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n -= 1
    return jokes_list


print(get_jokes(15, True))
