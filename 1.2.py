cub_list = []
cub_list_v2 = []
for i in range(1, 1000, 2):
    cub_list.append(i ** 3)

all_s = 0

for index, value in enumerate(cub_list):
    summ = 0
    while value > 0:
        summ += value % 10
        value //= 10
    if summ % 7 == 0:
        all_s += cub_list[index]
print(all_s)

for b in cub_list:
    cub_list_v2.append(b + 17)

all_s = 0

for index, value in enumerate(cub_list_v2):
    summ = 0
    while value > 0:
        summ += value % 10
        value //= 10
    if summ % 7 == 0:
        all_s += cub_list[index]

print(all_s)
