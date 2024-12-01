n = int(input())
a = (n + 1) / 2
b= (n - 1) / 2
for i in range(1, int(a) + 1):
    for j in range(1):
        print('*' * i)
    print()
for i in range(1, int(b)):
    for j in range(1):
        print('*' * j)
    print()