import multiprocessing


def factorize(*number):
    result_numbers = [[div_num for div_num in range(1, i + 1) if i % div_num == 0] for i in number]
    return result_numbers[0] if len(number) == 1 else result_numbers


if __name__ == '__main__':

    with multiprocessing.Pool(3) as pool:
        a, b, c, d = pool.map(factorize, (128, 255, 99999, 10651060))

    print(a, b, c, d, sep='\n')
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]