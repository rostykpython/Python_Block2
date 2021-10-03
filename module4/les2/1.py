import threading
import time
import concurrent.futures


class BankAccount:
    def __init__(self):
        self.balance = 100
        self.lock_obj = threading.Lock()

    def update(self, transaction: str, amount) -> None:
        print(f'Transaction {transaction} started')
        self.lock_obj.acquire()
        cash_amount = self.balance
        cash_amount += amount
        time.sleep(2)
        self.balance = cash_amount
        self.lock_obj.release()
        print(f'transaction ended: {transaction}')


if __name__ == '__main__':
    acc = BankAccount()
    print(f'Process started, balance = {acc.balance}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(acc.update, ('refill', 'withdraw'), (100, -200))
        # executor.map(acc.update, ('refill', 100), ('withdraw', -200))
    print(f'End = {acc.balance}')