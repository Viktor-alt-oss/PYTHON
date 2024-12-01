# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
# Формат входных данных
# На вход программе подаётся натуральное число 𝑛 — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.

n = int(input())
matrix = []
for i in range(n):
    elem = [int(num) for num in input().split()]
    matrix.append(elem)
li = []    
for r in range(n):
    for c in range(n):
        if r == c or r + c + 1 == n or (r > c and r < n - 1 - c) or (r < c and r > n - 1 - c):
            li.append(matrix[r][c])
        
print(max(li))
