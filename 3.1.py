translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
             'four': 'четыре', 'five': 'пять', 'six':
                 'шесть', 'seven': 'семь', 'eight': 'восемь',
             'nine': 'девять', 'ten': 'десять'}


def number_translate(w):
    return translate.get(w)


print(number_translate(input('Введите число для перевода: ')))
