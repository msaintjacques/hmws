def gen_sort(l):
    for i in l:
        if l.count(i) == 1:
            yield i

l = gen_sort([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])