import concurrent.futures
import time


def div(divisor, limit):
    print(f'started div = {divisor}')
    counter = 0
    for x in range(1, limit):
        if x % divisor == 0:
            counter += 1
            time.sleep(0.2)
    return counter


if __name__ == '__main__':
    print('started main')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        result = executor.map(div, (2, 5, 4, 10), (10, 25, 108, 209))
        print(list(result))


