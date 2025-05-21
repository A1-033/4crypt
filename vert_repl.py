import textwrap as tx
import numpy as np
# вводные
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-'
txt = '_ш.тзпктендиттдов,сеиаеаеичи_л_ым___яёдейел_киал_неоиноыумнф_оирпеанън_._ит_сктшус_рткпуинаъзь.окоие_ау_е.осс_тн_зъ'
key = [2,1,5,4,3]   # ключ байт

print('\n длина строки')
print(len(txt))

# разбиваем шифртекст на подстроки по 5 символов, если в последней подстроке меньше 5 символов, добиваем их заглушкой
def str_to_5ch(string, pad_char='а'):
    parts = tx.wrap(string, 5)
    # добавляем символы в последний элемент, если симовлов меньше 5
    list_indexes = []
    for el in parts:
        if len(el) < 4:
            el = el + pad_char * (5 - len(el))
        list_indexes.append(el)
    return list_indexes

words = str_to_5ch(txt)



print('\n Шифртекст, разбитый на подстроки по 5 символов')
print(words)

# Создаём массив 23x5, заполняемый по вертикали
arr = np.array(list(txt)).reshape(5, 23).T
#
# print("Вертикальный массив 24×5:")
# print(arr)

# Ключ для перестановки столбцов (нумерация с 1)
key = [2, 1, 5, 4, 3]  # Новый порядок столбцов: 2→1, 1→2, 5→3, 4→4, 3→5

# Преобразуем ключ в индексы (нумерация с 0)
col_indices = [i-1 for i in key]

# Переставляем столбцы
rearranged_arr = arr[:, col_indices]

print("Исходный массив (первые 5 строк):")
print(arr)
print("\nМассив после перестановки столбцов (первые 5 строк):")
print(rearranged_arr)