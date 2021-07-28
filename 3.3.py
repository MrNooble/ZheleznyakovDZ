def thesarus(*args):
    names_dict = {}
    for i in sorted(args):
        _mom = i[0]
        if _mom in names_dict:
            names_dict[_mom] += [i]
        else:
            names_dict[_mom] = [i]

    return names_dict


print(thesarus('Иван', 'Мария', 'Петр', 'Илья', 'Марина', 'Алина',
               'Бубочка'))
