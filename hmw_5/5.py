from random import randint

def write():
    f = open("5.txt", "w")

    for i in range(0, randint(0, 101)):
        f.write(str(randint(0, 200)) + " ")

    f.close()

def calc_sum():
    f = open("5.txt", "r")
    r = list(f.read().split(" "))
    f.close()

    result = sum(map(int, r[:len(r)-1]))
    print(f"Сумма чисел в файле: {result}")


write()
calc_sum()