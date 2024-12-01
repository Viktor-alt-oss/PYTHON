import random
list = [1, 2, 3, 4, 5]
print(dir(random)) 
print(help(random.choice))
print(random.randint(1,50))
random.sample(list, 2) # сколько чисел
random.choice(list) # выбор одного 