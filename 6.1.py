with open("logs.txt", "r", encoding="utf-8") as f:
    final_log = ((line.split()[0], line.split()[5][1:], line.split()[6]) for line in f)
    for i in final_log:
        print(i)
