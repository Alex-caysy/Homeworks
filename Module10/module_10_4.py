import threading
import time
import random
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
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest.start()
                    break
            if guest.is_alive():
                continue
            self.queue.put(guest)
            print(f'{guest.name} в очереди.')

    def discuss_guests(self):
        table_busy = True
        while not self.queue.empty() or table_busy:
            for guest in guests:
                for table in self.tables:
                    if guest.name == table.guest and not guest.is_alive():
                        print(f'\n{guest.name} покушал(-а) и ушёл(ушла)')
                        table.guest = None
                        print(f'Стол номер {table.number} свободен')

                    if not self.queue.empty() and not table.guest:
                        guest_from_queue = self.queue.get()
                        table.guest = guest_from_queue.name
                        print(f'{guest_from_queue.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        guest_from_queue.start()

                    if table.guest is None:
                        table_busy = False
                    else:
                        table_busy = True


tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
