digit = int(input())
str(c) = digit % 10
str(b) = (digit % 100) // 10
str(a) = digit // 100
print(a, b, c, '\n', a, c, b, '\n', b, a, c, '\n', b, c, a, '\n', c, a, b, '\n', c, b, a, sep='')



