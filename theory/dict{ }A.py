a = dict()
b = { 'Name': 'Ford Prefect',
 'Gender': 'Male',
 'Occupation': 'Researcher',
 'Home Planet': 'Betelgeuse Seven' }
found = {}
found[a] = 0
info = b.get('salary', 'Информации о зарплате нет')

info1 = {'name': 'Bob',
        'age': 25,}
info2 = {'age': 30, # добавляет age 30
        'city': 'New York',}
info1.update(info2) # или |=

info = {'name': 'Bob',
        'age': 25}
name1 = info.setdefault('name')           # параметр default не задан           
name2 = info.setdefault('name', 'Max')    # параметр default задан
print(name1)
print(name2)

del info['email'] 
job = info.pop('job') # возвращает значение, удаление по ключу
info_copy = info.copy() 
# Метод popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение)
# Метод clear() удаляет все элементы из словаря.
len(), sum(), min(), max()