"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""
while True:
    x = input('Введите целое число для x: ')
    y = input('Введите целое число для y: ')
    if x.isdigit() and y.isdigit:
        x = int(x)
        y = int(y)
        break
    else:
        print('Ошибка ввода, попробуйте снова!')

def my_func(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Деление на ноль'
