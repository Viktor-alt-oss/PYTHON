n = input()
flag = 'Цифр нет'
for i in n:
    if i in '0123456789':
        flag = 'Цифра'
        break
print(flag)