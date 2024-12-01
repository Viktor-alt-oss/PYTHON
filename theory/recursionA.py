def rec(x): # рекурсия замыкается 
    if x < 4:
        print(x)
        rec(x + 1)
        print(x)
rec(1)

def fact(x): # факториал с помощью рекурсии
    if x == 1:
        return 1
    return fact(x - 1) * x

print(fact(4))

def fib(x): # фибоначи с помощью рекурсии
    if x == 1:
        return 0
    if x == 2:
        return 1
    return fib(x-2) + fib(x-1)
print(fib(5))

def palindrom(s): # является ли строка палиндромом
    m = s.lower()
    if len(m) <= 1:
        return True
    if m[0] != m[-1]:
        return False
    return palindrom(s[1:-1])
print(palindrom('Шалаш'))

def rec(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1] 
print(rec('аваапавпвп'))

def power(x,n): # возведение числа в степень
    if n == 0:
        return 1
    if n < 0:
        return 1/power(x, -n)
    if n % 2 == 0:
        return power(x, n//2) * power(x, n//2)
    else:
        return power(x, n - 1) * x

def levels(n, level=1):
    print(n, 'level=', level)
    for i in n:
        if type(i) is 'list':
            levels(i, levels + 1)
num = [[[1, 2, 3, 4, 1, 2, 5, 4, 3]]]
levels(num)

def words(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        return s[0] + '*' + s[-1]
    return s[0] + '*' + words(s[1:-1]) + '*' + s[1]

print(words('LItBseoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO'))

def f(x):
    if len(x)==0:
        return x
    if x[0]=='(':
        return x[0] + f(x[1:]) + ')' 
    return x[0] + f(x[1:]) + x[0]

x='(((t((p((y((kx((((e(((((((vw((v(e((v(m(((h(mlx((s((((d(y((((((((mtk(d(umi((s((sx(p((m(r((kqo'
print(f(x))

import os 
name_folder = r'C:\Users\virgi\work\Python\draft'

print(os.listdir(name_folder))
for i in os.listdir(name_folder):
    print(i, type(i), name_folder + '\\' + i, os.path.isdir(name_folder + '\\' + i))



