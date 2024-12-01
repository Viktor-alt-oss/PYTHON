# Напишите функцию get_next_prime(num),
# которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

# объявление функции
def get_next_prime(num):
    for i in range(num + 1, num + 100):
        counter = 0
        for j in range(1, i + 1):
            if i % j == 0:
                counter += 1
        if counter == 2:
            return i

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))