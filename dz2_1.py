my_list = [5, 3.21, complex(5, 6), 'привет', [1, 2, 3], (5, 8, 9), {5, 8, 9}, {'key1': 500, 100: 51}, True, b'text', None, ZeroDivisionError ]

print(my_list)

for i in my_list:
    print(f'Элемент списка {i} имеет класс {type(i)}')

