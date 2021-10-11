from multiprocessing import Process
import time


class Count_and_print(Process):
    def __init__(self, n):
        super(Count_and_print, self).__init__()
        self.n = n

    def run(self) -> None:
        for i in range(self.n):
            self.n = self.n - 1
            print(self.n, 'left')
            time.sleep(1)


if __name__ == '__main__':
    p = Count_and_print(10)
    l = Count_and_print(5)
    l.start()
    p.start()

    print('how many left?')