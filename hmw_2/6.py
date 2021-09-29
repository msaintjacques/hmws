# классов явно не хватает)
struct = []
counter = 0

while True:
    print("[*] Начините ввод информации о новом товаре 👇🏻")

    name = input("\t[*] Название товара: ")
    price = input("\t[*] Цена: ")
    quantity = input("\t[*] Кол-во: ")
    unit = input("\t[*] Ед.: ")

    struct.append((counter, {
        "название": name,
        "цена": price,
        "кол-во": quantity,
        "ед.": unit,
    }))
    counter += 1

    inpt = input("[*] Наберите stop, если хотите прекратить, или Enter, если нужно заполнить информацию о след. товаре: ")
    if inpt == "stop":
        break
    else:
        continue

names = []
for i in struct:
    names.append(i[1].get("название"))

prices = []
for i in struct:
    prices.append(i[1].get("цена"))

quantitys = []
for i in struct:
    quantitys.append(i[1].get("кол-во"))

units = []
for i in struct:
    units.append(i[1].get("ед."))

analytics = {
    "название": names,
    "цена": prices,
    "количество": quantitys,
    "ед.": units,
}

print(analytics)