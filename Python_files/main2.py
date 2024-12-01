with open(r"C:\Users\virgi\Downloads\forbidden_words.txt") as inp, open(r"C:\Users\virgi\Downloads\data (1).txt", encoding='utf-8') as out:
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
