import textwrap as tx

# вводные
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-'
txt = '.нпыэз-окчурэбсувкачдчгвъйчср_е_ухзьвцасбёсымпехщьнщнфьчс,ыээчхатаойцжбмий_цжоыфапж,эж.гйщкизыкчоббм.к,жёйонпнптцнцз'
key = []
len_last_key = 0

# разбиваем шифртекст на подстроки по 6 символов, если в последней подстроке меньше 6 символов, добиваем их заглушкой
def str_to_6ch(string, pad_char='а'):
    parts = tx.wrap(string, 6)
    # добавляем символы в последний элемент, если симовлов меньше 6
    list_indexes = []
    for el in parts:
        if len(el) < 6:
            global len_last_key
            len_last_key = 6 - len(el)
            el = el + pad_char * len_last_key
        list_indexes.append(el)
    return list_indexes
words = str_to_6ch(txt)
print('\n Шифртекст, разбитый на подстроки по 6 символов')
print(words)

# переводим символы в числовые значения
def str_to_numbers(string, alphabet):
    char_to_num = {char: idx for idx, char in enumerate(alphabet)}
    # print(char_to_num)
    list_indexes = []
    for char in string:
        ind = []
        for el in char:
            ind.append(char_to_num[el])
        list_indexes.append(ind)
    return list_indexes
print('\n Числовые значения символов (подстроки по 6 символов)')
numbers = str_to_numbers(words, alphabet)
print(numbers)

initial_key=[9, 18, 19, 9, 14, 0] #истина

def autokey_decrypt_vectors(encrypted_vectors, initial_key_vector, alphabet_size=37):
    """
    Расшифровка списка векторов методом автоключа
    Параметры:
    encrypted_vectors - список векторов по 6 чисел (шифртекст)
    initial_key_vector - начальный ключ (вектор из 6 чисел)
    alphabet_size - размер алфавита (по умолчанию 37)
    Возвращает:
    Список расшифрованных векторов
    """
    decrypted_vectors = []
    key = initial_key_vector.copy()  # Копируем ключ, чтобы не менять оригинал
    for vector in encrypted_vectors:
        if len(vector) != 6:
            raise ValueError("Все векторы должны содержать ровно 6 чисел")
        decrypted_vector = []
        for i in range(6):
            # Формула расшифровки: (C - K) mod alphabet_size
            decrypted_num = (vector[i] - key[i]) % alphabet_size
            decrypted_vector.append(decrypted_num)
        key = [x for x in decrypted_vector]
        decrypted_vectors.append(decrypted_vector)
    return decrypted_vectors

decrypted_text = autokey_decrypt_vectors(numbers, initial_key, alphabet_size=37)
print(f"\n Расшифрованный список в виде ключей по 6 значений:")
print(decrypted_text)

# сделаем обратное преобразование индексов в символы
def num_to_chars(list, alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-'):
    list_symbols = []
    for el in list:
        ind = alphabet[el[0]], alphabet[el[1]],alphabet[el[2]], alphabet[el[3]],alphabet[el[4]], alphabet[el[5]]
        list_symbols.append(ind)
    return list_symbols
keys = num_to_chars(decrypted_text, alphabet)
print('\n Ключи, соответствующие парам шифртекста')
print(keys)

#
# # приведем символы к строке
def chars_to_string(simbols):
    fin_str=''
    for el in simbols:
        fin_str += ''.join(el)
        # так как мы в одной из функций добавляли символы для корректного вычитания ключей, сейчас их убираем, len_last_key = 4
    new_fin_str = fin_str[:-len_last_key]
    return new_fin_str
print('\n Итоговая расшифрованная строка')
ne_str = chars_to_string(keys)
print(ne_str)