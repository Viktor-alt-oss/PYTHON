y, x, y1, x1 = int(input()), int(input()), int(input()), int(input())# put your python code here
if y1 == y + 1 or y1 == y - 1 and x1 == x + 2 or x1 == x - 2:
    print('YES')
elif y1 == y + 2 or y1 == y - 2 and x1 == x + 1 or x1 == x - 1:
    print('YES')
else:
    print('NO')
    