# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами
# должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    __color = None

    def change_light(self, color):
        self.__color = color

    def out_red(self):
        print("\033[31m {}".format(self.__color))

    def out_yellow(self):
        print("\033[33m {}".format(self.__color))

    def out_green(self):
        print("\033[32m {}".format(self.__color))

    def out_clear(self):
        print("\033[0m {}".format(''))

    def running(self):
        self.__color = 'Красный'
        self.out_red()
        time.sleep(7)
        self.__color = 'Желтый'
        self.out_yellow()
        time.sleep(2)
        self.__color = 'Зеленый'
        self.out_green()
        time.sleep(5)
        self.out_clear()


my_trafficLight = TrafficLight()
my_trafficLight.running()
print('Завершено')
