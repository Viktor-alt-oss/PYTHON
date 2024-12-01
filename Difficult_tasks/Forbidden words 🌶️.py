# На вход программе подается строка текста с именем текстового файла. 
# Напишите программу, выводящую на экран содержимое этого файла, но с заменой всех запрещенных слов звездочками * 
# (количество звездочек равно количеству букв в слове).
# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. 
# Гарантируется, что все слова в этом файле записаны в нижнем регистре.

with open('forbidden_words.txt', encoding='utf-8') as inp, open(input(), encoding='utf-8') as out:
    taboo = inp.read().split()
    s = out.read()
    s_lower = s.lower()
    for t in taboo:
        s_lower = s_lower.replace(t, '*'*len(t))
    for r in range(len(s)):
        if s_lower[r] == '*':
            print('*', end='')
        else:
            print(s[r], end='')