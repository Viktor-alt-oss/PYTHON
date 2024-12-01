import random

# Константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

# Просим пользователя ввести данные 
n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
add_digit = input('Включить цифры? (д = да, н = нет) ').strip()
add_lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
add_uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
remove_badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет) ').strip()

# Настройка генерируемых паролей
if add_digit[0].lower() == 'д':
    chars += digits
if add_lowercase[0].lower() == 'д':
    chars += lowercase_letters
if add_uppercase[0].lower() == 'д':
    chars += uppercase_letters
if add_punctuation[0].lower() == 'д':
    chars += punctuation
if remove_badsymbols[0].lower() == 'д':
    for c in 'il1Lo0O?':
        chars = chars.replace(c, '')

# Вводим функцию
def generate_password(n, length):
    mi = ''
    for _ in range(n):
        for _ in range(length):
            mi += random.choice(chars)
        mi += '  '
    return mi
            
print(generate_password(n, length))
