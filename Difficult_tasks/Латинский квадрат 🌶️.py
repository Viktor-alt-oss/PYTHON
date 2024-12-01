# Латинским квадратом порядка 𝑛 называется квадратная матрица размером n×n, каждая строка и каждый столбец которой содержат все числа от 1 до 𝑛. 
# Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.

import copy
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
li = []
for c in range(n):
    elem = []
    for r in range(n):
        elem.append(matrix[r][c])
    li.append(elem)
flag = 'YES'
for i in range(n):
    totality1 = [i for i in range(1, n + 1)] 
    totality2 = copy.deepcopy(totality1)
    counter1 = 0
    counter2 = 0
    total1 = ''
    total2 = ''
    for j in range(n):
        if matrix[i][j] in totality1 and str(matrix[i][j]) not in total1:
            counter1 += 1
            total1 += str(matrix[i][j])
        if li[i][j] in totality2 and str (li[i][j]) not in total2:
            counter2 += 1
            total2 += str(li[i][j])
        else:
            flag = 'NO'
            break
    if counter1 != n or counter2 != n:
        flag = 'NO'
        break
            
print(flag)