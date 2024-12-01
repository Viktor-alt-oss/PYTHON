# На вход программе подается строка текста, содержащая символы. 
# Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

s = input().split()
li = []
elem = [s[0]]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        elem.append(s[i])
    elif s[i] != s[i-1]:
        li.append(elem)
        elem = [s[i]]
li.append(elem)
print(li)