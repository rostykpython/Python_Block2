import multiprocessing


def square_sum(my_list, result):

    for idx, num in enumerate(my_list):
        result[idx] = num**2

    print(f'Result of process P1: {result[:]}')


if __name__ == '__main__':

    my_list1 = [i for i in range(5)]
    result1 = multiprocessing.Array('i', 5)

    p1 = multiprocessing.Process(target=square_sum, args=(my_list1, result1))

    p1.start()
    p1.join()

    print(f"Result of main program: {result1[:]}")
    print(result1)
