import multiprocessing
import os


def worker1():
    print(f'ID worker 1: {os.getpid()}')

def worker2():
    print(f'ID of worker2: {os.getpid()}')


if __name__ == '__main__':

    print(f'ID of main process: {os.getpid()}')

    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    p1.start()
    p2.start()

    print(f'ID of process1: {p1.pid}')
    print(f'ID of process2: {p2.pid}')
    print(f'P1, P2 status {p1.is_alive(), p2.is_alive()}')

    p1.join()
    p2.join()

    print("end of execution")
    print(f'P1, P2 status {p1.is_alive(), p2.is_alive()}')
    