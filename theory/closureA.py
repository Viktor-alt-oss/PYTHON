def main_func(value):
    name = value # Можно main_func(name)
    def inner_func():
        print('hello my friend', name)
    
    return inner_func

a = main_func('Ivan')
a()

def adder(value):

    def inner(a):
        return value + a
    return inner

a2 = adder(2)
print(a2(10))

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

a3 = counter()
print(a3())
print(a3())

def average_numbers(): #среднее арефметическое 
    numbers = []
    def inner(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)
    return inner

r1 = average_numbers()
print(r1(5))
print(r1(15))

d2 = average_numbers()
print(d2(100))

def average_num(): #cреднее арефметическое
    counter = 0
    summa = 0
    def inner(number):
        nonlocal summa
        nonlocal counter
        summa += number
        counter += 1
        return summa / counter
    return inner
from time import perf_counter, sleep
def timer(): # таймер
    start = perf_counter()
    def inner():
        return perf_counter() - start
    return inner

s1 = timer()
sleep(2)
print(s1())
sleep(1)
print(s1())

def plus(a, b):
    return a + b

def many(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} количество раз')
        return (func(*args, **kwargs))
    return inner

c1 = many(plus)
print(c1(10, 20))
print(c1(30, 40))
    

n1 = average_num()
print(n1(20))
g = 'gray'
def colors(param='r'):
    y = 'yellow'   
    g = 'fray'
    def blue():
        nonlocal y
        b = 'синий'
        y = 'welliw'
        print(b, y, g)
    blue() if param == 'r' else print("i don't know")

colors(32)