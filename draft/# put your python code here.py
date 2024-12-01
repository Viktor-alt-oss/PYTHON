def merge(list1, list2):
    list1.extend(list2)
    return list1.sort()
   

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))


