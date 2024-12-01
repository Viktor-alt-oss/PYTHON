# объявление функции
def draw_triangle():
    for i in range(8):
        for j in range(1):
            j = ' ' * (8 - 1 - i) + '*' * (1 + i * 2)
            print(j)
            

# основная программа
draw_triangle()  # вызов функции