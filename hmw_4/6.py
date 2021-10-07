from itertools import count, cycle

def gen_count(v):
    max_num = v + 1000

    for i in count(v):
        if i >= max_num:
            break
        yield i

def gen_cicle(l):
    counter = 0

    for i in cycle(l):
        if counter >= len(l):
            break
        counter += 1
        yield i