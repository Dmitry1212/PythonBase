# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# pip install translate
from translate import Translator
translator = Translator(from_lang="English", to_lang="Russian")

try:
    file = open('numbers.txt', 'r', encoding='utf-8')
    file_out = open('numbers_out.txt', 'w', encoding='utf-8')
    for line1 in file:
        if line1 != '':
            temp = line1.split()
            temp[0] = translator.translate(temp[0])
            line1 = ' '.join(temp) +'\n'
        file_out.write(line1)

    file.close()
    file_out.close()
except:
    print('Ошибка чтения файла')
