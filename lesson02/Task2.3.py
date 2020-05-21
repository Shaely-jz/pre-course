"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

while True:
    month = input('Введите месяц в виде целого числа от 1 до 12: ')
    if month.isdigit() and int(month) in range(1, 13):
        month = int(month)
        break
    else:
        print('Не соответствует условию. Попробуйте снова.')

list_of_seasons = ['зима', 'весна', 'лето', 'осень']
index = month // 3 % 4
print('Решение через список: ', list_of_seasons[index])

dict_of_seasons = {'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
for key, value in dict_of_seasons.items():
    if month in value:
        print('Решение через словарь: ', key)
        break
