def print_res(l):
    print(f"Строк в файле: {len(l)}")

    for line_num, line in enumerate(l):
        print(f"Строка {line_num+1}) Слов - {line}")

f = open("2.txt", "r")
lines = []

for line in f.readlines():
    lines.append(len(line.split(" ")))
f.close()

print_res(lines)