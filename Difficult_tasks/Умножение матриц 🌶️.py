# Напишите программу, которая перемножает две матрицы.

n1, m1 = [int(i) for i in input().split()]
matrix1 = [[int(i) for i in input().split()] for _ in range(n1)]
input()
n2, m2 = [int(i) for i in input().split()]
matrix2 = [[int(i) for i in input().split()] for _ in range(n2)]
matrix3 = [[0] * m2 for _ in range(n1)]

for r in range(n1):
    for c in range(m2):
        for k in range(m1):
            matrix3[r][c] += matrix1[r][k] * matrix2[k][c]
        
        
for x in matrix3:
    print(*x)