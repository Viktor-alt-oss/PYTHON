n = int(input())
for i in range(1, n + 1, 1):
    for j in range(i):
        if (j + 1) / 2 <= i / 2:
            print(j + 1, end='')
       