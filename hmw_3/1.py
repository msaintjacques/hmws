def div(arg_1, arg_2):
    if arg_2 == 0:
        return 0

    return arg_1 / arg_2

num_1 = float(input("Введите первое число: "))
num_2 = float(input("Введите второе число:"))

print(f"Результат деления {num_1} на {num_2} = {div(num_1, num_2)}")