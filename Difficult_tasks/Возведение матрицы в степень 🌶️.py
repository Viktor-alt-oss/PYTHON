# Напишите программу, которая возводит квадратную матрицу в 𝑚-ую степень.

import copy
n = int(input())
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
matrix_copy = copy.deepcopy(matrix1)
degree = int(input())
for _ in range(degree - 1):
    matrix2 = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            for k in range(n):
                matrix2[r][c] += matrix1[r][k] * matrix_copy[k][c] 
    matrix1 = matrix2
        



for x in matrix2:
    print(*x)