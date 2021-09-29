seasons = [
    "Зима",
    "Весна",
    "Лето",
    "Осень",
]

ui = int(input("Введите номер месяца: "))

if ui == 12 or ui >= 1 and ui <= 2:
    print(seasons[0])
elif ui >= 3 and ui <= 5:
    print(seasons[1])
elif ui >= 6 and ui <= 8:
    print(seasons[2])
elif ui >= 9 and ui <= 11:
    print(seasons[3])
else:
    print("Кажется, вы ввели лишнюю цифру")