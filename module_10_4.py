import threading
import time
from random import randint
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(3, 10))

class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        for new_guest in guests:
            guest_is_sitting = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = new_guest
                    guest_is_sitting = True
                    guest = Guest(new_guest).start()
                    print(f'{new_guest.name} сел(-а) за стол номер {table.number}')
                    break

            if not guest_is_sitting:
                self.queue.put(new_guest)
                print(f'{new_guest.name} в очереди')

    def discuss_guests(self):
       while True:
            is_empty_tables = True
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\n', f'Стол номер {table.number} свободен')
                    table.guest = None
                elif table.guest is not None:
                    is_empty_tables = False
                elif not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
            if self.queue.empty() and is_empty_tables:
                break

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()