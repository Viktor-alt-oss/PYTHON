def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1  # Убираем младшую единицу
        count += 1
    return count

print(count_set_bits(13)) 
