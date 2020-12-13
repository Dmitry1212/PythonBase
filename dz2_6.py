base = [(1, {'название': 'компьddddddютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
        (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
        (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
        ]
menu1 = '\n1 - просмотр базы\n\
2 - добавление товара\n\
3 - аналитика\n\
4 - выход'

print('Добро пожаловать в базу данных магазина')
print('*' * 50)

while True:
    print(menu1)
    action = int(input('Ваши действия: '))
    if action == 1:
        print('*' * 50)
        print(f'Номер    Наименование    Цена   На складе')
        for i in base:
            print(f'{i[0]:3}  - {i[1]["название"][:13]:>14} {i[1]["цена"]:>8} {i[1]["количество"]:>4} {i[1]["eд"]:^4}')
    elif action == 2:
        print('*' * 50)
        print('Введите данные о новом товаре')
        temp = base[0][1].copy()

        for k in temp.keys():
            temp[k] = input(f'{k}: ')

        base.append((len(base) + 1, temp))
    elif action == 3:
        print('*' * 50)
        print('Аналитика по базе данных')
        temp = base[0][1]       # для хранения ключей
        output_temp = []        # временный список
        output = {}             # выходной

        for k in temp.keys():   # цикл по ключам
            for el in base:     # цикл по элементам списка
                output_temp.append(el[1][k])
            output[k] = set(output_temp)
            output_temp = []

        for key in output:
            print(f'{key}: {output[key]}')


    elif action == 4:
        print('*' * 50)
        print('До свидания!')
        break
    else:
        print('не корректный ввод команды')
