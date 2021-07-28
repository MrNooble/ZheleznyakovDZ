duration = int(input("Ввести секунды: "))
min = duration // 60
hour = duration // 3600
day = duration // 86400
mons = duration // 2629743
year = duration // 31556926
if duration < 60:
    print(duration, "сек.")
elif duration >= 60 and duration < 3600:
    print(min, "мин.", duration % 60, "сек.")
elif duration >= 3600 and duration < 86400:
    print(hour, "час.", duration % 3600 // 60, "мин.", duration % 60, "сек.")
elif duration >= 86400 and duration < 2629743:
    print(day, "дн.", hour % 24, "час.", duration % 3600 // 60, "мин", duration % 60, "сек.")
