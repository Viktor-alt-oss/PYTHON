from collections import Counter
s = 'adsvcvsdfaa'
letters = Counter(s)
print(letters)
print(tuple(letters.values()))
for i in letters.elements():
    print(i)

print(letters.most_common())

r = Counter()
for i in [1, 1, 1, 2, 2, 2, 3, 4, 4, 4]:
    r[i] += 1
print(r)

d = Counter([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5])
print(d)

print(r + d)