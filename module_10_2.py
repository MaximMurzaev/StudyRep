import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.fight_days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies:
            self.enemies -= self.power
            time.sleep(1)
            self.fight_days += 1
            print(f'{self.name} сражается {self.fight_days}, осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {self.fight_days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
