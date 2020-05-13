# Задавать вопросы, пока пользователь не введёт верный ответ
name = input('Имя создателя Python: ')

while name != 'Гвидо':
    print('Неверно')
    name = input('Имя создателя Python: ')

print('Верно')

# Вариант с использованием break

name = None

while True:
    name = input('Имя создателя Linux: ')
    if name == 'Линус':
        break
    print('Неверно')

print('Верно')
