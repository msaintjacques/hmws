def fact(to):
    res = 1
    for i in range(1, to+1):
        res *= i
        yield res