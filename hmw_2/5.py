lst = lst = [7, 5, 3, 3, 3, 2]

print(f"[*] Рейтинг: {lst}")
print("[*] Начните вводить по-одному элементы")

while True:
    inpt = input("[*] Введите значение, или stop, чтобы завершить ввод: ")

    if inpt == "stop":
        break
    elif not inpt.isdigit():
        print("\t[!] Была введено не число, элемент не был добавлен, введите другое значение")
        continue
    elif inpt.isdigit():
        if inpt in lst:
            lst.insert(lst.index(inpt) + lst.count(inpt) - 1, int(inpt))
        else:
            lst.append(int(inpt))
        lst.sort()
        lst.reverse()
        print(f"\t [*] Вы ввели: {inpt}, текущий рейтинг: {lst}")