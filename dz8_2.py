# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
# на нуль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


in_data_1 = input('Введите делимое: ')
in_data_2 = input('Введите делитель: ')

try:
    in_data_1 = int(in_data_1)
    in_data_2 = int(in_data_2)
    if in_data_2 == 0:
        raise MyOwnErr("Ты что? Низзя на ноль делить!")
    print(f'Результат деления: {in_data_1/in_data_2}')
except (ValueError, MyOwnErr) as err:
    print(err)
