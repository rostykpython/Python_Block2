# Daemon

import multiprocessing
import time
import sys


def daemon():
    p = multiprocessing.current_process()
    print(f'Starting {p.pid}, {p.name}')
    sys.stdout.flush()
    time.sleep(2)
    print(f'Exiting {p.pid}, {p.name}')
    sys.stdout.flush()


def non_daemon():
    p = multiprocessing.current_process()
    print(f'Starting {p.pid}, {p.name}')
    sys.stdout.flush()
    time.sleep(2)
    print(f'Exiting {p.pid}, {p.name}')
    sys.stdout.flush()


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non_daemon', target=non_daemon)

    n.daemon = False

    d.start()
    time.sleep(2)
    n.start()

