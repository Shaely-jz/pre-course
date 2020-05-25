"""
3. Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
"""

def my_func1(x, y, z):
    my_list = [x, y, z]
    my_list.pop(my_list.index(min(my_list)))
    return sum(my_list)

print('Сумма наибольших двух аргументов: ', my_func1(3, 8, -2))
