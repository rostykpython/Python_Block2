# Process pool
import os
import time
from multiprocessing import Pool


def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s


if __name__ == '__main__':
    numbers = range(25000)
    start = time.perf_counter()

    with Pool(processes=8) as p:
        p.map(sum_square, numbers)

    finish = time.perf_counter()

    print(f'Execution time: {finish-start} sec')
    print(f'Threads {os.cpu_count()}')