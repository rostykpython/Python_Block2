import concurrent.futures
import time


def div(divisor, limit):
    print(f'started div = {divisor}')
    for x in range(1, limit):
        if x % divisor == 0:
            print(f'division={divisor}, x={x}')
            time.sleep(0.2)

    print(f'End: {divisor}\n')


if __name__ == '__main__':
    print('started main')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(div, 3, 25)
        executor.submit(div, 5, 25)
        executor.submit(div, 2, 10)
        print('Printed after submit')

    print('Proccess finished')

