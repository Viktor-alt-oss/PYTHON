num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
        break
if flag:
    print('Число простое')
else:
    print('Число составное')