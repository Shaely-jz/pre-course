"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
biggest_num = 0
num = int(input('Введите целое положительное число: '))

while num and biggest_num != 9:
    tmp = num % 10
    if tmp > biggest_num:
        biggest_num = tmp
    num //= 10

print('Наибольшая цифра в этом числе: ', biggest_num)
