# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(x, y):
    if y == 0:
        return 'деление на ноль'
    return x/y


while True:
    act = (input('Осуществить деление? (Y/N)')).upper()

    if act == 'Y':
        try:
            a = int(input('Делимое: '))
            b = int(input('Делитель: '))
            print(f'Результат деления: {division(a, b)}')
        except:
            print('Ошибка ввода! Попробоуйте еще раз')
    elif act == 'N':
        break
    else:
        print('Ошибка ввода! Попробоуйте еще раз')