"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""

string = input("Введите строку из нескольких слов, разделённых пробелами: ")

for i, word in enumerate(string.split(' '), 1):
    print(f'{i}) {word[:10]}')
