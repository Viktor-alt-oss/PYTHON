from math import log
total = 0
n = int(input())
for i in range(1, n):
    total += 1 / i

print(total - log(n))
