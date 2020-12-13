try:
    vir = int(input('сколько выручка: '))
    izd = int(input('а издержек: '))

    prib = vir - izd

    if prib > 0:
        print('Фирма работает с прибылью!')
        print(f'Рентабельность: {prib / vir:.2f}')

        n = int(input('Численность сотрудников: '))
        print(f'На одного сотрудника доход составил: {prib/n:.1f}')

    elif prib < 0:
        print('Фирма работает в убыток!')
    else:
        print('Фирма работает в ноль!')

except:
    print('ошибка! некорректный ввод\n'
          'попробуйте еще раз \n')
