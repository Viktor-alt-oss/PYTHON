# put your python code here
def math_e(num, mun):
    a = num + mun
    b = num - mun
    c = num * mun
    d = num / mun
    e = num // mun
    f = num % mun
    g = (num ** 10 + mun ** 10)** 0.5
    return a, b, c, d, e, f, g
    
n, m = int(input()), int(input())
print(*math_e(n, m), sep='\n')