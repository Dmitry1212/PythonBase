# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.
from abc import ABCMeta, abstractmethod, abstractproperty
import re


class Storage:
    def __init__(self):
        self.warehouse = []

    def __str__(self):
        st = '\n На складе находится: \n'
        for i in self.warehouse:
            st += str(i[0].name) + '\n' + str(i[1]) + f' штук(а/и) хранится на {i[2]} \n\n'
        return st

    def set_new_pos(self, item, n, place='склад'):
        temp = [item, n, place]
        if Storage.check_new(*temp):
            self.warehouse.append(temp)
        pass

    def send(self, i, new_plase):           # пока допущение, что передается все имеющееся количество
        self.warehouse[i][2] = new_plase    # в базе остается информация, куда передали обоудование
        pass

    @staticmethod
    def check_new(item, n, place):
        try:
            if not n > 0:
                return False
        except:
            print("Ошибка ввода")

        return True
        pass

    @property  # количество записей
    def cnt(self):
        return len(self.warehouse)

    @property  # количество единиц товара
    def cnt_all(self):
        n = 0
        for i in self.warehouse:
            if i[2] == 'склад':
                n += i[1]
        return n


class OrgTech:
    def __init__(self, n, p, m=False, l1='A4'):
        self.name = n  # название
        self.price = p  # цена
        self.letter_size = l1  # размер бумаги
        self.mono = m  # монохромность

    @abstractmethod
    def __str__(self):
        pass

    # @abstractmethod
    # def input_new(self):
    #     pass


class Printer(OrgTech):
    def __init__(self, n, p, m, l1, load, t):
        super().__init__(n, p, m, l1)
        self.load = load  # допустимая нагрузка листов в месяц
        self.type = t  # тип: лазерный/струйны

    def __str__(self):
        return f'Принтер {self.name}: \n Стоимость {self.price}, допустимый размер бумаги: {self.letter_size} \n \
               {"монохромный" if self.mono else "Цветной"}, {self.type}, \
                допустимая нагрузка листов в месяц: {self.load}'

    # def input_new(self):
    #     self.name = input("Ввведите название: ")
    #     try:
    #         self.price = input('Стоимость: ')
    #     except ValueError:
    #         print('Ошибка')


class Scanner(OrgTech):
    def __init__(self, n, p, m, res, l1, lamp):
        super().__init__(n, p, m, l1)
        self.lamp = lamp  # вид лампы: свотодиодная/галогеновая
        self.resolution = res  # разрешение сканирования

    def __str__(self):
        return f'Сканер {self.name}: \n Стоимость {self.price}, допустимый размер бумаги: {self.letter_size} \n ' \
               f'{"монохромный" if self.mono else "Цветной"}, {self.lamp}, ' \
               f' разрешение сканирования: {self.resolution}'


# class Xerox(Printer, Scanner):                                # ромбовидное наследование потом
#     def __init__(self, n, p, m, res, l1, load, s, t, lamp):
#         super(Printer, self).__init__(n, p, m, l1, load, t)
#         super(Scanner, self).__init__(res, lamp)
#         self.scale = s  # максимальное масштабирование

class Xerox(OrgTech):
    def __init__(self, n, p, m, l1,  s, ):
            super().__init__(n, p, m, l1)
            self.scale = s  # максимальное масштабирование

    def __str__(self):
        return f'Ксерокс {self.name}: \n Стоимость {self.price}, допустимый размер бумаги: {self.letter_size} \n ' \
               f'{"монохромный" if self.mono else "Цветной"},  ' \
               f'максимальное масштабирование {self.scale}'


class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


printer = Printer('HP', 3000, False, 'A4', 10000, 'laser')
scanner = Scanner('Canon', 2000, False, 10000, 'A4', 'Diode')
xerox = Xerox('Xerox', 5500, False,  'A4',  500)

print(printer)
print(scanner)
print(xerox)

sklad = Storage()
sklad.set_new_pos(printer, 1)
sklad.set_new_pos(printer, 3)
sklad.set_new_pos(scanner, 2)
sklad.set_new_pos(xerox, 2)
sklad.send(2, 'office 2')
# print(sklad)
print(f'В базе найдено {sklad.cnt} записей')
print(f'На складе хранится {sklad.cnt_all} штук товара')
