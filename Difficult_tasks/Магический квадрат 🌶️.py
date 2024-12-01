# Магическим квадратом порядка 𝑛 называется квадратная таблица размера n × n, составленная из всех чисел 1, 2, 3, … , 𝑛^2 так, 
# что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. 
# Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

n = int(input())
ma = []  # по строкам
for i in range(n):
    elem = [int(num) for num in input().split()]
    ma.append(elem)

na = [] # по столбцам
for c in range(n):
    el = []
    for r in range(n):
        el.append(ma[r][c])
    na.append(el)
    
counter = sum(ma[0])
flag = 'YES' 
to = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
d1 = 0
d2 = 0
for m in ma:
    if counter != sum(m):
        flag = 'NO'
        break
    for a in m:
        if a in to:
            to.remove(a)
            total += 1
            
sum_main_diag = 0
sum_semi_diag = 0
for i in range(n):                           
        sum_main_diag += ma[i][i]
        sum_semi_diag += ma[i][n - 1 - i] 
        
if sum_main_diag != sum_semi_diag != counter:
    flag = 'NO'
if total != 9:
    flag = 'NO'  
    
for n in na:
    if counter != sum(n):
        flag = 'NO'
        break

print(flag)