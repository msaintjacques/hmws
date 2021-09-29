user_input = []

print("[*] Начните вводить по-одному элементы")
while True:
    inpt = input("[*] Введите значение, или stop, чтобы завершить ввод: ")
    if inpt == "":
        print("\t[!] Была введена пустая строка, элемент не был добавлен, введите другое значение")
        continue
    if inpt == "stop":
        break
    user_input.append(inpt)

counter = 0
while counter <= len(user_input)-2:
    if counter != len(user_input):
        user_input[counter], user_input[counter + 1] = user_input[counter + 1], user_input[counter]
    counter += 2

print(f"[*] Результат: {user_input}")