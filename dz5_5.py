# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

res = [randint(0, 10) for x in range(25)]
print(res)

line1 = ''
for i in res:
    line1 += str(i) + ' '

file = open('text_5_5.txt', 'r+', encoding='utf-8')
file.write(line1)
file.seek(0)

sum1 = 0
for i in file:
    temp = list(map(int, i.split()))
    for j in temp:
        sum1 += j
    print(f'Сумма чисел в строке: {sum1}')

file.close()
