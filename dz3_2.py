# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def opros(name, surname, birthday, city, email, phone):
    return f'{name} {surname} родился {birthday} в проживает в {city} \nКонтактные данные:\nТелефон: {phone} \nПочта: {email}'


print(opros(name='Вася', surname='Петров', birthday='31/02/1905', city='Каштаново', email='petrov-cool@yayaya.ru',
            phone='+7(908)908-98-98'))
