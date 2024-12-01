import random
print('Добро пожаловать  в числовую угадайку')

def is_valid(sim):
    return sim.isdigit()

def game():
    while True:
        print('Напишите правую границу:')
        num = input()
        if is_valid(num):  
            n = random.randint(1, int(num))
            break
        else:
            print('А может быть все-таки введем целое число')
        
    
    print(f"Напишите число от 1 до {num}")    
    counter = 0
    while True:
        s = input()
        if is_valid(s):
            s = int(s)
            counter += 1
            if s == n:
                print('Вы угадали, поздравляем!')
                print('количество попыток:', counter)
                break    
            elif s < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif s > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'А может быть все-таки введем целое число от 1 до {num}?')         
            
game() 
print("Если хотите продолжить игру напишите 'да' или 'нет' ")
word = input()
while True:
    if word[0].lower() == 'д':
        game()
        print("Если хотите продолжить игру напишите 'да' или 'нет' ")   
        word = input()
    elif word[0].lower() == 'н':
        break
    else:
        print('Напиши правильно')
        word = input()
    
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


# Для напоминания как работает функция с выводом полученного значения

# def is_valid_r():                    
#    print('Напиши правую границу') 
#    n = input()
#    if n.isdigit() and int(n) > 1:
#        return int(n)
#    else:
#        print('Напиши правильно')
        
# is_valid_r()
# n = is_valid_r()
# print(10 - n)
        


       
