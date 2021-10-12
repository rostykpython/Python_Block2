import multiprocessing


def factorize(*numbers):
    result = []
    for number in numbers:
        local_res = []
        for div_num in range(1, number + 1):
            if number % div_num == 0:
                local_res.append(div_num)
        result.append(local_res)
    return result[0] if len(numbers) == 1 else result


if __name__ == '__main__':
    with multiprocessing.Pool(3) as pool:
        a, b, c, d = pool.map(factorize, (128, 255, 99999, 10651060))

    print(a, b, c, d, sep='\n')
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]
