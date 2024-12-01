n = int(input())
s = input()
for c in s:
    k = (ord(c) - n + 26) % 26
    print(chr(k), end='')