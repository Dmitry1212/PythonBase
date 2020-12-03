try:
    n = input('введите число: ')
    out = int(n)+int(n+n)+int(n+n+n)
    print(out)

except:
    print('ошибка! некорректный ввод\n'
          'попробуйте еще раз \n')