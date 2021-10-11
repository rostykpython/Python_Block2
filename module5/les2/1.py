import multiprocessing

result = []


def square_sum(my_list):
    global result

    for i in my_list:
        result.append(i**2)

    print(f'Result process: {result}')


if __name__ == '__main__':
    my_list = [1, 2, 3, 4]

    p1 = multiprocessing.Process(target=square_sum, args=(my_list,))
    
    p1.start()

    p1.join()

    print(f'Result in main process: {result}')