import random
n = random.randint(1, 100)
print('Добро пожаловать  в числовую угадайку')

def is_valid(sim):
    return sim.isdigit() and 0 < int(sim) < 101

print("Напишите число от 1 до 100")
counter = 0
while True:
    s = input()
    if is_valid(s):
        s = int(s)
        counter += 1
        if s == n:
            print('Вы угадали, поздравляем!')
            print('количество попыток:', counter)
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break    
        elif s < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif s > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')

        
    
    
    
    
    
    
    




    