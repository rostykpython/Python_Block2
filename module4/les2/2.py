import threading as trd
import time

lock_obj = trd.RLock()


#
# print("Acquired first time")
# lock_obj.acquire()
#
# print('Acquiring second time')
# lock_obj.acquire()
#
# print('Realising')
# lock_obj.release()


a = 5
b = 5
a_lock = trd.Lock()
b_lock = trd.Lock()

def calc():
    global a
    global b

    print('T1 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)
    print('T2 acquiring lock b')
    b_lock.acquire()

    a += 5
    b += 5

    a_lock.release()
    b_lock.release()

def calc2():
    global a
    global b

    print('T1 acquiring lock a')
    a_lock.acquire()
    time.sleep(5)
    print('T2 acquiring lock b')
    b_lock.acquire()

    a += 5
    b += 5

    b_lock.release()
    a_lock.release()


if __name__ == '__main__':
    t1 = trd.Thread(target=calc)
    t2 = trd.Thread(target=calc2)

    t1.start()
    t2.start()