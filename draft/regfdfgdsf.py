# put your python code here
n = int(input())
ma = []
for i in range(n):
    elem = [int(num) for num in input().split()]
    ma.append(elem)

na = []
for c in range(n):
    el = []
    for r in range(n):
        el.append(ma[r][c])
    na.append(el)
    
counter = sum(ma[0])
flag = 'YES' 
to = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for m in ma:
    if counter != sum(m):
        flag = 'NO'
        break
    for a in m:
        if a in to:
            to.remove(a)
            total += 1
if total != 9:
    flag = 'NO'        
for n in na:
    if counter != sum(n):
        flag = 'NO'
        break
qw = 0
for x in range(n):
    qw += ma[x][x]
if qw == counter:
    flag = 'YES'

print(flag)
    
