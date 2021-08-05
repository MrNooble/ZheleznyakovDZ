from itertools import islice, zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']

final_rez = (i for i in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(type(final_rez))
print(*islice(final_rez, 9))
print(list(islice(final_rez, 3)))
