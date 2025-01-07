import threading
import random
import time
from threading import Thread, Lock

class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            y = random.randint(50, 500)
            self.balance += y
            print(f"Пополнение: {y}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for j in range(100):
            b = random.randint(50, 500)
            print(f"Запрос на {b}")
            if b <= self.balance:
                self.balance -= b
                print(f"Снятие: {b}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')