# put your python code here
def sd(x):
    n = x.split('.')
    total = 0
    for i in range(len(n) - 1):
        total += int(n[i]) * 256**(len(n) - 1 - i)
    return total
def gem(word):
    total = 0
    l = list(map(int, word.split('.')))
    l.reverse()
    for index, i in enumerate(l):
        total += i * (256 ** index)
    return total
print(*sorted([input() for _ in range(int(input()))], key=sd), sep='\n')
def pretty_print(data, side='-', delimiter='|'):
    count = 0
    for i in data:
        count += 1
    print(f' {side * (count + ((len(data) + 1) * 2))}')
    print(delimiter, end=' ')
    for j in data:
        print(j, delimiter, end=' ')
    print()
    print(f' {side * (count + ((len(data) + 1) * 2))}')