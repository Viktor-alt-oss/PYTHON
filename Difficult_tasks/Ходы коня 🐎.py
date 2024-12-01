# На шахматной доске 8 × 8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьёт конь. 
# Клетку, где стоит конь, отметьте английской буквой N, а клетки, которые бьёт конь, отметьте символами *, остальные клетки заполните точками.

a = 'abcdefgh'
b = '87654321'
elem = [['.'] * 8 for _ in range(8)]
symbol = [i for i in input()]
r = symbol[0]
cols = a.find(r)
c = (symbol[1])
rows = b.find(c) 
li = []
for i in range(8):
    for j in range(8):
        if i == rows and j == cols:
            elem[i][j] = 'N'
        if rows - i == 2:
            if j - cols == 1 or cols - j == 1:
                elem[i][j] = '*'
        if rows - i == 1:
            if j - cols == 2 or cols - j == 2:
                elem[i][j] = '*'        
        if i - rows == 2:
            if j - cols == 1 or cols - j == 1:
                elem[i][j] = '*'
        if i - rows == 1:
            if j - cols == 2 or cols - j == 2:
                elem[i][j] = '*'
                        
        
for m in elem:
    print(*m)