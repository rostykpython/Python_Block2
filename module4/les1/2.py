from threading import Thread
import time


class CountAndPrint(Thread):
    def __init__(self, n, daemon=True):
        super(CountAndPrint, self).__init__()
        self.n = n

    def run(self) -> None:
        for i in range(self.n):
            print(self.n - i, 'left')
            time.sleep(0.5)


t = CountAndPrint(10)
t.start()

print('How many have left?')