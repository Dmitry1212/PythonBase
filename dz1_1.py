Privetstvie = 'Что делаем: \n\
 1 - сложим\n\
 2 - вычтем\n\
 3 - умножим\n\
 4 - разделим\n\
 5 - выход: '

while True:
    try:
        make = int(input(Privetstvie))
    except:
        print('ошибка! некорректный ввод\n'
              'попробуйте еще раз \n')
        continue

    if not (make >= 1) and (make <= 5):
        print('ошибка! такого не умею\n'
              'попробуйте еще раз \n')
        continue

    try:
        if make != 5:
            a = int(input('оператор 1: '))
            b = int(input('оператор 2: '))
    except:
        print('ошибка! операторы не корректны \n\
              вводите числа')
        continue

    if make == 1:
        print(f'сумма {a + b} \n\n')
    elif make == 2:
        print(f'разность {a - b} \n\n')
    elif make == 3:
        print(f'умножение {a * b} \n\n')
    elif make == 4:
        print(f'частное {a / b} \n\n')
    elif make == 5:
        print('До свидания, \n\
        Спасибо, что воспользовались услугами нашего сервиса')
        break
    else:
        print('До свидания, \n')
