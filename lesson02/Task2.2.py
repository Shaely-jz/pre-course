"""
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

word = list(input("Введите любое слово: "))
i = 1
while i < len(word):
    word[i], word[i - 1] = word[i - 1], word[i]
    i += 2

print(word)
