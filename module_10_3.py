import threading
import time
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            rand_num = randint(50, 100)
            self.balance += rand_num
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {rand_num}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rand_num = randint(50, 100)
            print(f'Запрос на : {rand_num}.')
            if rand_num <= self.balance:
                self.balance -= rand_num
                print(f'Снятие: {rand_num}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств!')
                self.lock.acquire()
bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')