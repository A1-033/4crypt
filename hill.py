import numpy as np

# Вводные
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-'
txt = 'йхгдквё_оеанзчкбяёешлксжаэсся,кгсэампамыглш.цвбъмч_ло_ыпыли,вюу.чщп,.ъёъчтчфуеффыьсяафаищщ,ющяоеыфёънесхыкц_.коъаезз'
k_inv = [
    [14, 13],
    [12, 25]
]

def split_to_pairs(text, pad_char='х'):
    """
    Разбивает текст на пары символов. Если длина нечётная, добавляет pad_char в конец.

    :param text: строка для разбивки
    :param pad_char: символ для дополнения (по умолчанию 'х')
    :return: список пар символов
    """
    if len(text) % 2 != 0:
        text += pad_char  # Добавляем символ, если длина нечётная
    return [text[i:i + 2] for i in range(0, len(text), 2)]
print('\n Шифртекст, разбитый на пары')
encrypted_pairs = split_to_pairs(txt)
print(encrypted_pairs)

def char_to_num(chars, alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-'):
    """
    Переводит пару символов в их числовые индексы в алфавите
    :param chars: список пар символов
    :param alphabet: строка с алфавитом (по умолчанию русский + символы)
    :return: список пар индексов
    """
    list_indexes = []
    for el in chars:
        ind = alphabet.index(el[0]), alphabet.index(el[1])
        list_indexes.append(ind)
    return list_indexes
print('\n Ключи, соответствующие парам шифртекста')
ind = char_to_num(encrypted_pairs, alphabet)
print(ind)

def hill_decrypt_pair(ind, k_inv, mod=37):
    """
    Расшифровывает пару символов методом Хилла
    :param pair: кортеж (int, int) - индексы зашифрованных символов
    :param inv_key_matrix: обратная матрица ключа [[a, b], [c, d]]
    :param mod: модуль (по умолчанию 37)
    :return: кортеж (int, int) - индексы расшифрованных символов
    """
    list_new_ind = []
    for el in ind:
        a, b = el
        # Умножение матрицы на вектор
        x = (k_inv[0][0] * a + k_inv[1][0] * b) % mod
        y = (k_inv[0][1] * a + k_inv[1][1] * b) % mod
        list_new_ind.append((x, y))
    return list_new_ind
new_ind = hill_decrypt_pair(ind, k_inv)
print('\n Расшифрованные пары по методу Хилла с помощью формул умножения')
print(new_ind)

# второй вариант, тоже рабочий, делал для проверки

# def hill_decrypt_pair_np(ind, k_inv, mod=37):
#     """
#     Умножает вектор на матрицу с использованием NumPy с применением модуля.
#     Параметры:
#         vector:  вектор [x, y] из списка
#         matrix: list или np.array - матрица [[a, b], [c, d]]
#         mod: int - модуль (по умолчанию 37)
#     Возвращает:
#         np.array - результат умножения с модулем [r1, r2]
#     """
#     # Преобразуем входные данные в массивы NumPy
#     vector = np.array(ind, dtype=np.int64)
#     matrix = np.array(k_inv, dtype=np.int64)
#     # Выполняем умножение вектора на матрицу
#     result = np.dot(vector, matrix) % mod
#     return result
#
# new_ind_np = hill_decrypt_pair_np(ind, k_inv, mod=37)
# print('\n Расшифрованные пары по методу Хилла с помощью NumPy')
# print(new_ind_np)

# сделаем обратное преобразование индексов в символы
def num_to_chars(nums, alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-'):
    list_symbols = []
    for el in nums:
        print(el)
        ind = alphabet[el[0]], alphabet[el[1]]
        list_symbols.append(ind)
    return list_symbols
print('\n Ключи, соответствующие парам шифртекста')
ind = num_to_chars(new_ind, alphabet)
print(ind)

# приведем символы к строке
def chars_to_string(inds):
    result = ''.join(char for pair in inds for char in pair)
    print(result)
print('\n Итоговая расшифрованная строка')
chars_to_string(ind)