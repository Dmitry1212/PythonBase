try:
    sourse = int(input('время в секундах: '))
    print(f'Время: {((sourse // 3600) % 60):02}:{((sourse // 60) % 60):02}:{(sourse % 60):02}')

except:
    print('ошибка! некорректный ввод\n')

