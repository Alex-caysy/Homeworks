import time
import threading


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self) -> None:
        print(f'{self.name}, на нас напали!')
        enemies = 100
        count_day = 0
        while enemies:
            time.sleep(1)
            enemies -= self.power
            count_day += 1
            print(f'{self.name} сражается {count_day} день(дня)..., осталось {enemies} воинов.')
        print(f'{self.name} одержал победу спустя {count_day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
