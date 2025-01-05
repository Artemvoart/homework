import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.name} сражается {days} суток, осталось {enemies} воинов врага.')
        print(f'{self.name} одержал победу спустя {days} дней(я)!')


knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight('Sir Galahad', 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончены!')