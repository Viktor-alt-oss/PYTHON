n = int(input())
max_digit = 0
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit: #1
            max_digit = digit #2
    n = n // 10 #3
if max_digit == 0: #4
    print('NO')
else:
    print(max_digit)