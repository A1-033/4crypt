# Определяем алфавит (символ -> число)
alphabet = {
    'а': 0, 'б': 1, 'в': 2, 'г': 3, 'д': 4, 'е': 5, 'ё': 6, 'ж': 7, 'з': 8, 'и': 9,
    'й': 10, 'к': 11, 'л': 12, 'м': 13, 'н': 14, 'о': 15, 'п': 16, 'р': 17, 'с': 18, 'т': 19,
    'у': 20, 'ф': 21, 'х': 22, 'ц': 23, 'ч': 24, 'ш': 25, 'щ': 26, 'ъ': 27, 'ы': 28, 'ь': 29,
    'э': 30, 'ю': 31, 'я': 32, '_': 33, '.': 34, ',': 35, '-': 36
}

# Обратный алфавит (число -> символ)
reverse_alphabet = {v: k for k, v in alphabet.items()}

# Параметры шифра
a = 14
b = 12
a_inv = 8  # Обратный элемент для a=14 mod 37
mod = 37


def affine_decrypt(char):
    """Дешифрует один символ"""
    if char in alphabet:
        c = alphabet[char]
        p = (a_inv * (c - b)) % mod
        return reverse_alphabet[p]
    return char  # Возвращаем символ как есть, если его нет в алфавите

def print_decryption_table(encrypted_text):
    """Выводит таблицу соответствия символов"""
    print("\nТаблица соответствия символов:")
    print("┌───────────────┬───────────────┐")
    print("│ Зашифрованный │ Расшифрованный│")
    print("├───────────────┼───────────────┤")

    for char in encrypted_text:
        decrypted_char = affine_decrypt(char)
        print(f"│ {char.center(13)} │ {decrypted_char.center(13)} │")

    print("└───────────────┴───────────────┘")


# Пример использования
if __name__ == "__main__":
    encrypted_text = "дчрюсгхэазлцмосщпхзьясе-лшеепфсрешлинли.ряьжбгщуиоэяаэ.н.яъфгв_жоёнфжухуотой_зйй.кеплйлъёёфвёпаз.йхуцзеч.сбэжсаулзмм"
    print(f"Зашифрованный текст: {encrypted_text}")
    print_decryption_table(encrypted_text)

    # Дополнительно выводим полный расшифрованный текст
    decrypted_text = ''.join([affine_decrypt(c) for c in encrypted_text])
    print(f"\nПолный расшифрованный текст: {decrypted_text}")
