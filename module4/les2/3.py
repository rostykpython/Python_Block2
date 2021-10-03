import threading as trd
import time


def consumer(cond):
    print('Starting consumer thread')

    with cond:
        cond.wait()
        print('Resource is available')


def producer(cond: trd.Condition):
    print('Started producer thread')
    with cond:
        print('Making resource available')
        cond.notify_all()


condition = trd.Condition()

t1 = trd.Thread(name='consumer1',target=consumer, args=(condition,))
t2 = trd.Thread(name='consumer2', target=consumer, args=(condition,))
p = trd.Thread(name='producer', target=producer, args=(condition,))

t1.start()
time.sleep(2)
t2.start()
time.sleep(2)
p.start()
