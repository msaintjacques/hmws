def pow(x, y):
    res = x
    for i in range(0, (-1*y)-1):
        res *= x

    return 1/res

x = int(input("Введите основание степени: "))
y = int(input("Введите показатель степени: "))

print(pow(x, y))