# Напишите функцию is_palindrome(text), 
# которая принимает в качестве аргумента строку text и возвращает значение True если указанный текст является палиндромом и False в противном случае.

# объявление функции
def is_palindrome(text):
    s = [i.lower() for i in text if i.isalpha()]
    return s[::1] == s[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))