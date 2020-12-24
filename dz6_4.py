# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
import random

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False
    direction = ['Налево', 'Направо', 'Назад']

    def __init__(self, s, c, n):
        self.speed = s
        self.color = c
        self.name = n

    def go(self):
        print('Поехали')

    def stop(self):
        print('Остановились')

    def turn(self):
        print(f'Повернули {random.choice(self.direction)}')

    def show_speed(self):
        return self.speed

    def set_speed(self, s):
        self.speed = s


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        return self.speed if (self.speed < self.speed_limit) else 'Превышение скорости'


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        return self.speed if (self.speed < self.speed_limit) else 'Превышение скорости'


class PoliceCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)
        is_police = True


town_c = TownCar(20, 'green', 'Paz')
print(f'Автомобиль {town_c.name}:')
print(f'Скорость: {town_c.show_speed()}')
town_c.go()
town_c.set_speed(70)
town_c.turn()
town_c.stop()
print(f'Скорость: {town_c.show_speed()}\n\n')

sport_c = SportCar(100, 'green', 'Mazda')
print(f'Автомобиль {sport_c.name}:')
print(f'Скорость: {sport_c.show_speed()}')
sport_c.go()
sport_c.set_speed(120)
sport_c.turn()
sport_c.stop()
print(f'Скорость: {sport_c.show_speed()} \n\n')


work_c = WorkCar(20, 'green', 'Lexus')
print(f'Автомобиль {work_c.name}:')
print(f'Скорость: {work_c.show_speed()}')
work_c.go()
work_c.set_speed(120)
work_c.turn()
work_c.stop()
print(f'Скорость: {work_c.show_speed()} \n\n')

police_c = PoliceCar(100, 'blue', 'RolsRoise')
print(f'Автомобиль {police_c.name}:')
print(f'Скорость: {police_c.show_speed()}')
police_c.go()
police_c.set_speed(120)
police_c.turn()
police_c.stop()
print(f'Скорость: {police_c.show_speed()} \n\n')
