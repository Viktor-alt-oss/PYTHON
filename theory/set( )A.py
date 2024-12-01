a = set()
b = {1, 2, 3, 4}
numbers = {2, 4, 6, 8, 10}
languages = {"Python", "C#", "C++", "Java"}
mammals = {"cat", "dog", "fox", "elephant"}
myset1 = set(range(10))          # множество из элементов последовательности
myset2 = set([1, 2, 2, 2, 3, 4, 5])    # множество из элементов списка
myset3 = set('abcd')             # множество из элементов строки
myset4 = set((10, 20, 30, 40))   # множество из элементов кортежа
myset1 = {1, 2, [5, 6], 7}  # множество не может содержать список
myset2 = {1, 2, {5, 6}, 7}  # множество не может содержать множество
myset = {1, 2, (5, 6), 7}  # множество может содержать кортеж

numbers = {1, 1, 2, 3, 5, 8, 3}  # создаем множество
numbers.add(21)  # добавляем число 21 в множество
numbers.add(34)  # добавляем число 34 в множество

numbers.remove('wwsd') # вызывает ошибку, если такого значения нет
numbers.discard('wwsd') # не вызывает ошибку
num = numbers.pop() # удаляет случайный элемент множества, возвращая его
# Метод clear() удаляет все элементы из множества

myset3 = myset1.union(myset2) # | или myset1.update(myset2) |=
myset3 = myset1.intersection(myset2) # & или myset1.intersection_update(myset2) &=
myset3 = myset1.difference(myset2) # - или myset1.difference_update(myset2) -=
myset3 = myset1.symmetric_difference(myset2) # ^ или myset1.symmetric_difference_update(myset2) ^=

set1 = {2, 3}
set2 = {1, 2, 3, 4, 5, 6}
print(set1.issubset(set2)) # < или <=
print(set2.issupper(set1)) # > или >=
# Для определения отсутствия общих элементов в множествах используется метод isdisjoint()
len(), sum(), min(), max()