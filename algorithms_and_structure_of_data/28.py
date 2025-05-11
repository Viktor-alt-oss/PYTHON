def climbStairs(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return climbStairs(n - 1) + climbStairs(n - 2)

n = 5

print(climbStairs(n))


def ways(n):
    # Базовые случаи
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    # Рекурсивный случай
    return ways(n - 1) + ways(n - 2) + ways(n - 3) + ways(n - 4)

# Пример использования
n = 5  # число ступенек
print(f"Количество способов подняться по лестнице из {n} ступенек: {ways(n)}")