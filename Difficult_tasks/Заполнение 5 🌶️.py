# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m, заполнив её в соответствии с образцом.

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        matrix[r][c] = (r + c) % m + 1

for i in matrix:
    for m in i:
        print(str(m).ljust(3), end='')
    print()