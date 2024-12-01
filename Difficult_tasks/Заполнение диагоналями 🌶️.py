# На вход программе подаются два натуральных числа 𝑛 и 𝑚. Напишите программу, которая создает матрицу размером n×m, заполнив её "диагоналями" в соответствии с образцом.

n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

nm = 0
for q in range(n*m):
    for i in range(n):
        for j in range(m):
            if i+j == q:
                nm += 1 
                matrix[i][j] = nm
                
for m in matrix:
    for n in m:
        print(n, end=' ')
    print()