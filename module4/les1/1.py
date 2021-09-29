from threading import Thread
from time import sleep


class MyThread(Thread):

    def __init__(self, second_num):
        super().__init__()
        self.delay = second_num

    def run(self):
        sleep(self.delay)
        print('Wake up!')


t = MyThread(2)
t.start()

print('Usefull message')
