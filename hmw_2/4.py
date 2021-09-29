user_input = input("Введите слова через пробел: ")

if len(user_input) != 0:
    for el in list(user_input.split(" ")):
        print(el if len(el) <= 10 else el[:10])
else:
    print("Вы ничего не ввели 😬")