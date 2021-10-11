def calc():
    result = {}
    f = open("6.txt", "r")

    for line in f.readlines():
        if len(line.split(":")) > 0:
            d = map(lambda el: el if el.isdigit() else 0, line.replace("(", " ").split())
            result[line.split(":")[0]] = sum(map(int, d))
    f.close()

    return result

res = calc()
print(f"Результат: {res}")