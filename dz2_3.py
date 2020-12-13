Mounth = int(input('Введите номер месяца (от 1 до 12): '))

SeasonsList = ['Зима', 'Весна', 'Лето', 'Осень']

print('Через list: ')
if (Mounth <= 2) or (Mounth == 12):
    print(f'Вы указали сезон: {SeasonsList[0]}')
elif (Mounth >= 3) and (Mounth <= 5):
    print(f'Вы указали сезон: {SeasonsList[1]}')
elif (Mounth >= 6) and (Mounth <= 8):
    print(f'Вы указали сезон: {SeasonsList[2]}')
elif (Mounth >= 9) and (Mounth <= 11):
    print(f'Вы указали сезон: {SeasonsList[3]}')


MounthDict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
              9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}

print('\nЧерез dict: ')
print(f'Вы указали сезон: {MounthDict[Mounth]}')


# второй вариант
print('\nЧерез dict с другой структурой: ')
SeasonsDict2 = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

for key in SeasonsDict2:
    for i in SeasonsDict2[key]:
        if i == Mounth:
            print(f'Вы указали сезон: {key}')
