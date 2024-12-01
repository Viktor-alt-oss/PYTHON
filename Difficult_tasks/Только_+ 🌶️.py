#Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

a, b, c = int(input()), int(input()), int(input())
count = 0
if a > 0:
    count = count + a
if b > 0:
    count = count + b
if c > 0:
    count = count + c
print(count)