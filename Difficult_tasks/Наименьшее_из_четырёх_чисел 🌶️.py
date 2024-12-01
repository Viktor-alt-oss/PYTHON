#Напишите программу, которая определяет наименьшее из четырёх чисел.

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b:
    b = a
if c < d:
    d = c
if b < d:
    d = b
print(d)