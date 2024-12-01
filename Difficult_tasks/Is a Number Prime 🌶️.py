# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и возвращает значение True,
# если число является простым, или False в противном случае.
 
# объявление функции
def is_prime(num):
    counter = 0
    for i in range(2, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 1:
        return True
    else:
        return False
        

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
