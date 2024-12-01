list = []
list2 = [2, 34]
list3 = list2.copy()
list.append('a')
list.extend(list2)
list.pop() # удаление по индексу
list.insert(0, 1) # добавляет значение в указанный индекс
list.remove('wds') # удаляет первое вхождение значения
list.find('dsffds') # индекс первого вхождения 
list.count(3) # подсчет количества
list.reverse() # обратный порядок
del list[1]
print(list)
help(list)
s = 'help melp'
c = list(s)
m = ''.join(c)
li = s.split()
# Метод clear() удаляет все элементы из словаря.
len(), sum(), min(), max()

