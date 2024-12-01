# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True,
# если пароль является надежным и False - в противном случае.
# Пароль является надежным если:

# его длина не менее 8 символов; 
# он содержит как минимум одну заглавную букву (верхний регистр); 
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

def is_passwort_good(num):
    counter = len(num)
    c_A = 0
    c_a = 0
    c_1 = 0
    for i in num:
        if i.isupper():
            c_A += 1
        if i.islower():
            c_a += 1
        if i.isdigit():
            c_1 += 1
    if counter > 7 and c_A > 0 and c_a > 0 and c_1 > 0:
        return True
    else:
        return False
n = input()
print(is_passwort_good(n))
