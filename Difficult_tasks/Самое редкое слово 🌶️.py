# На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. 
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

n = [i.strip('/.?,;:"!') for i in input().lower().split()]
result = {}
for m in n:
    result[m] = result.get(m, 0) + 1
res = 10
word = 'www'
for key, value in result.items():
    if value < res:
        res = value
        word = key
    elif value == res:
        if key < word:
            res = value
            word = key
        
print(word)