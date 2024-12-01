# объявление функции
def is_prime(num):
    if num % 1 == 0 and num % num == 0:
        return True
    else:
        return False

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
n = int(input())