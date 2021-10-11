import multiprocessing
import os
import time
import multiprocessing
import functools

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def add(x, y):
    return x * y


def func(f):
    return f()


f_inc = functools.partial(inc, 4)

f_dec = functools.partial(dec, 2)

f_add = functools.partial(add, 3, 4)


if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        res = pool.map(func, [f_add, f_dec, f_inc])
        print(res)



