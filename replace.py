import textwrap as tx

# вводные
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя_.,-'
txt = 'ш_.тпзктнедиттдо,всеаиеаиечил__ы_м__ёядеейл_икалн_еониоымунфо_ирепаннъ_.и_т_кстшсу_рктпуниаъьз.оокиеа_у_.еос_стнз_ъъ'
key = [2,1,3,4]   # ключ байт

# разбиваем шифртекст на подстроки по 4 символов, если в последней подстроке меньше 4 символов, добиваем их заглушкой
def str_to_4ch(string, pad_char='а'):
    parts = tx.wrap(string, 4)
    # добавляем символы в последний элемент, если симовлов меньше 4
    list_indexes = []
    for el in parts:
        if len(el) < 4:
            el = el + pad_char * (4 - len(el))
        list_indexes.append(el)
    return list_indexes

words = str_to_4ch(txt)
print('\n Шифртекст, разбитый на подстроки по 4 символа')
print(words)

def repl(lists):
    key = [2, 1, 3, 4]
    new_lists = []
    for list in lists:
        new_list = list[1] + list[0] + list[2] + list[3]
        new_lists.append(new_list)
    return new_lists

print('\n Текст после выполнения перстановки по ключу "байт"')
rep_words = repl(words)
print(rep_words)

def chars_to_string(simbols):
    fin_str=''
    for el in simbols:
        fin_str += ''.join(el)
    return fin_str
print('\n Итоговая расшифрованная строка')
ne_str = chars_to_string(rep_words)
print(ne_str)