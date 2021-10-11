import multiprocessing
import time
import threading

start = time.perf_counter()


def func():
    print("Start counting")
    time.sleep(1)
    print('End counting')


if __name__ == '__main__':
    # multiprocessing.freeze_support()

    p1 = multiprocessing.Process(target=func)
    p2 = multiprocessing.Process(target=func)

    p1.start()
    p2.start()


    # p1 = threading.Thread(target=func)
    # p2 = threading.Thread(target=func)
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()


    finish = time.perf_counter()

    print(f'Finished at {round(finish - start)} sec')
