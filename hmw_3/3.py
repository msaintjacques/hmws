def my_func(num_1, num_2, num_3):
    args_l = sorted([num_1, num_2, num_3])

    return args_l[len(args_l) - 1] + args_l[len(args_l) - 2]
