# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):           # с замахом на то, что потом количество аргементов может быть любым
    sortlist = [a, b, c]
    sortlist.sort()
    l= len(sortlist)
    return sortlist[l-1]+sortlist[l-2]


while True:
    act = (input('Сложить два наибольших числа? (Y/N)')).upper()

    if act == 'Y':
        try:
            a = int(input('Первое число: '))
            b = int(input('Второе число: '))
            c = int(input('Третье число: '))
            print(f'Результат деления: {my_func(a,b,c)}')
        except:
            print('Ошибка ввода! Попробоуйте еще раз')
    elif act == 'N':
        break
    else:
        print('Ошибка ввода! Попробоуйте еще раз')
