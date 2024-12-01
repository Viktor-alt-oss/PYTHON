#Напишите программу, которая упорядочивает три числа от большего к меньшему.

a, b, c = int(input()), int(input()), int(input())
a1 = max(a, b, c)
b1 = min(a, b, c)
c1 = (a + b + c) - a1 - b1
print(a1)
print(c1)
print(b1)