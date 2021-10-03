import threading as trd
import time
import random


class NightClub:
    def __init__(self):
        self.bouncer = trd.Semaphore(3)

    def open_club(self):
        for i in range(1, 31):
            t = trd.Thread(target=self.guest, args=(i,))
            t.start()

    def guest(self, guest_id):
        print(f'\nGuest id: {guest_id} is waiting for entering the club')
        self.bouncer.acquire()
        print(f'\nGuest {guest_id} is doing dance')
        time.sleep(random.randint(1, 4))

        print(f'\nGuest {guest_id} is leaving the club')
        self.bouncer.release()


if __name__ == '__main__':
    club = NightClub()
    club.open_club()