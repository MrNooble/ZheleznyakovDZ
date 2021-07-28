translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
             'four': 'четыре', 'five': 'пять', 'six':
                 'шесть', 'seven': 'семь', 'eight': 'восемь',
             'nine': 'девять', 'ten': 'десять'}


def number_translate(w):
    if w.istitle():
        return str(translate.get(w.lower())).title()
    return translate.get(w)


print(number_translate(input('Введите число для перевода: ')))
