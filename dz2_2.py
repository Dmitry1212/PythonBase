temp = input('Введите элементы списка через пробел: ')
my_list = temp.split()
# my_list = ['25', '447', '58', '47', '478', '5']     #для тестирования

i = 0

while i + 1 < len(my_list):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2

print(my_list)
