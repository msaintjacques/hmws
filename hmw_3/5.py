print("Введите 'exit', чтобы остановить программу")

sum = 0
exit = False

while exit != True:
    nums = input("Введите числа через проблем: ")

    for i in nums.split(" "):
        if i == "exit":
            exit = True
            break

        sum += float(i)
    print(f"Сейчас сумма чисел равна: {sum}")

print(f"Результат: {sum}")

