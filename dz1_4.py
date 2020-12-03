n = int(input('Целое положительно число: '))
nm = 0

while True:
    temp = n % 10
    if nm < temp:
        nm = temp
    n //= 10
    if n == 0:
        break

print(f'Наибольшее число: {nm}')



