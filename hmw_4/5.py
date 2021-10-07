from functools import reduce

gen = (i for i in range(100, 1001) if i %2 == 0)
sum = lambda c, p: c + p

print(f"Сумма: {reduce(sum, gen)}")