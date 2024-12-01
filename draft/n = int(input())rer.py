n = int(input())
a = (n + 1) / 2
b= (n - 1) / 2
for i in range(1, int(a) + 1):
    for j in range(1):
        print('*' * i)
    print(end='')  
for i in range(int(b), 0, - 1):
    for j in range(1):
        print('*' * i)
    print(end='')