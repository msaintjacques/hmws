num = int(input("Введите число: "))
max_num = int(str(num)[0])

while num != 0:
    current_num = num % 10
    num //= 10

    if current_num > max_num:
        max_num = current_num
        if current_num == 9:
            break

print(max_num)
