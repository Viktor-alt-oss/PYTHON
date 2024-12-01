from math import log #cложный код
total = 0 
n = int(input())
for i in range(n):
    total += (1 / ( i  +  1))
   
print(total - log(n))