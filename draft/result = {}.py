import random

length = int(input())    # длина пароля
for _ in range(length):
    print(chr(random.randint(65, 122)), end='')
