a = [1, 2, 3] # итерируемый обьект
b = iter(a) # итератор 
print(next(b))
a = [i for i in range(6)] 
b = (i for i in range(6)) # выражение - генератор поддерживает один раз
print(next(b)) # генератор изначально является итератором
print(next(b))
print(next(b))
c = (i for i in range(10000)) # большая информация, выражения генераторы не хранят в себе информациют, а получают по одному значению
for s in c:
    print(s)
# применять !! Len(c) !! нельзя, c[10] индекс тоже нельзя применить
print(list(c))

def gaf():
    for i in [1, 2, 3]:
        yield i
s = gaf()
print(next(s))
print(next(s))



def factoriality(n): # факториал с помощью генератора
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield pr

for i in factoriality(10):
    print(i, end=' ')

def itr():
    yield from range(20)
for i in itr():
    print(i, end=' ')
