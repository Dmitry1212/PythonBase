# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import re


class Date:
    def __init__(self, d):
        self.date = d

    @classmethod
    def get_nums(cls, obj):
        return list(map(int, obj.date.split("-"))) if Date.check_data(obj) else 'Ошибка даты'

    @staticmethod
    def check_data(obj):
        if re.fullmatch(r"\d\d-\d\d-\d\d\d\d", obj.date):
            temp = obj.date.split('-')
            if 1 <= int(temp[0]) <= 31 and 1 <= int(temp[1]) <= 12 and 1900 < int(temp[2]) < 2100:  # общая проверка
                if re.fullmatch('04|06|09|11', temp[1]) and int(temp[0]) == 31:  # на 30 дней в месяце
                    return False
                if int(temp[1]) == 2:  # на февраль
                    if int(temp[0]) > 29:
                        return False
                    if int(temp[2]) % 4 != 0 and int(temp[0]) > 28:
                        return False
                return True
        else:
            return False


d = Date('29-02-2020')
print(d.date)
print(Date.check_data(d))
print(Date.get_nums(d))
