# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. 
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.

s = input().split()
total = ''
eng = 'abcdefghijklmnopqrstuvwxyz'
for c in s:
    if '"' in c :
        len_c = len(c) - 2
    elif c.isalnum():
        len_c = len(c)
    else:
        len_c = len(c) - 1
    for j in c:
        if j.isalnum() and j.islower():
            ind = eng.index(j)
            cj = eng[(ind + len_c) % 26]
            total += cj
        elif j.isalnum() and j.isupper():
            ind = eng.index(j.lower())
            cj = eng[(ind + len_c) % 26]
            total += cj.upper()
        else:
            total += j
    total += ' '
print(total)