"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

def salary():
    try:
        time, stavka, premia = map(int, argv[1:])
        print(f"Зарплата: {time * stavka + premia}")
    except ValueError:
        print("Enter all 3 numbers. Not string or.")

salary()