def print_res(m):
    sum = 0
    for wrkr in m.items():
        sum += float(wrkr[1].rstrip())
        if float(wrkr[1].rstrip()) <= 20:
            print(f"Сотрудник {wrkr[0]} получает менее 20к")

    print(f"Средняя зарплата: {sum / len(m)}")

f = open("3.txt", "r")
results = {}

for line in f.readlines():
    if len(line.split("-")) == 2:
        wrkr = line.split("-")
        results[wrkr[0]] = wrkr[1]
f.close()

print_res(results)
