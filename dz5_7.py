# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

output_firm = {}
out = []
sum1 = 0  # суммарная прибыль
cnt = 0  # число фирм с прибылью

try:
    with open('firms_info.txt', 'r', encoding='utf-8') as firms:
        for line1 in firms:
            if line1 != '':
                temp = line1.split()
                vir, izd = int(temp[2]), int(temp[3])
                if vir > izd:
                    sum1 += vir - izd
                    cnt += 1
                output_firm[temp[0]] = vir - izd
        print(f'Средняя прибыль по {cnt} фирмам: {sum1 / cnt}')
    out.append(output_firm)
    out.append({'Средняя прибыль': (sum1 / cnt)})
    print(out)

except:
    print('Ошибка чтения файла')

with open('firms_out.txt', 'w', encoding='utf-8') as firms:
    json.dump(out, firms, indent=3, ensure_ascii=False)