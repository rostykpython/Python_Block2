from threading import RLock, Thread
from time import time, sleep

lock = RLock()


def func(locker, delay):
    timer = time()
    locker.acquire()
    print('Hi')
    sum1 = 1 + 2
    print(sum1)
    sleep(delay)
    
    print('Done', time() - timer)


t1 = Thread(target=func, args=(lock, 2))
t2 = Thread(target=func, args=(lock, 2))

t1.start()
t2.start()
print('Started')