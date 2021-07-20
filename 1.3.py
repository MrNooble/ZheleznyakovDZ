for name in range(100):
    if name % 10 == 1 and name % 100 != 11:
        print(name, 'процента,', end=" ")
    elif 1 < name % 10 < 5 and not 11 < name % 100 < 15:
        print(name, 'процента,', end=" ")
else:
    print(name, 'процентов,', end= " ")
