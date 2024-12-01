empty_tuple = () # пустой кортеж
point = (1.5, 6.0) 
info = ('Timur', 'Guev', 28, 170, 60, False) # кортеж из 6 элементов разных типов
nested_tuple = (('one', 'two'), ['three', 'four']) # кортеж из кортежа и списка # список можно поменять, а кортеж нет
my_tuple = (1,) # один элемент
text = 'hello python'
str_tuple = tuple(text)

numbers = (2, 4, 6, 8, 10)
print(numbers[1:3])
print(numbers[2:5])

print((1, 2, 3, 4) + (5, 6, 7, 8))
print((7, 8) * 3)
print((0,) * 10)

a = (1, 2, 3, 4)
b = (7, 8)
a += b   # добавляем к кортежу a кортеж b
b *= 5   # повторяем кортеж b 5 раз 
print(a)
print(b)

names = ('Gvido', 'Roman' , 'Timur')
position = names.index('Timur') # Чтобы избежать ошибок, можно использовать метод index() вместе с оператором принадлежности in
cnt1 = names.count('Timur')

not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
print(not_sorted_tuple)

sorted_tuple = tuple(sorted(not_sorted_tuple))

tuple1 = ('Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si')
list1 = list(tuple1) # в список
string1 = ''.join(tuple1) # в строку

number = 12345
tpl = tuple(number)
print(tpl) # приведет к ошибке: TypeError: 'int' object is not iterable



len(), sum(), min(), max()