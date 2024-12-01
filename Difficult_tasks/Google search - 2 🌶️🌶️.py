#На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов,
# затем k строк — поисковые запросы.
# Напишите программу, которая выводит все введенные строки, в которых встречаются одновременно все поисковые запросы.

n = int(input())
l = list()
for _ in range(n):
    s = input()
    l.append(s)
k = int(input())
li = []
for _ in range(k):
    j = input()
    li.append(j)
for i in l:
    counter = 0
    for o in li:
        if o.lower() in i.lower():
            counter += 1
        if counter == k:
            print(i)