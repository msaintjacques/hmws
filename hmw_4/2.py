def gen_sort(l):
    curr = l[0]

    for i in l[1:]:
        if i > curr:
            yield i

        curr = i

l = gen_sort([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])
