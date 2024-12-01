#Дано натуральное число. 
# Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

n = int(input())
flag = True
last_digit = n % 10

while n > 0:
    if last_digit > n % 10:
        flag = False

    last_digit = n % 10
    n //= 10

if flag:
    print("YES")
else:
    print("NO")