#На вход программе подается натуральное число n и n строк, а затем число k.
# Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.

n = int(input())
l = []
string = ''
for _ in range(n):
    s = input()
    l.append(s)
k = int(input())
for i in range(len(l)):
    m = l[i]
    if k <= len(m):
        x = m[k-1]
        string += x
print(string)