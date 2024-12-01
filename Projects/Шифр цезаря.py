# Узнаем данные 
cod = input("Шифрование или дешифрование? Напиши 'ш' или 'д':  ").lower()
while cod != 'ш' and cod != 'д':
    cod = input("Введи правильно. Напиши 'ш' или 'д':  ").lower()
language = input("Русский или английский язык? Напиши 'р' или 'а':  ").lower()
while language != 'р' and language != 'а':
    language = input("Введи правильно. Напиши 'р' или 'а':  ").lower()
    
# Алфавиты   
eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
rus_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

if cod[0] == 'ш':
    s = input('Напишите текст для шифрования:  ')
    step = 'Вправо'
else:
    s = input('вставьте текст для дешифрования:  ')
    step = 'Влево'
if language[0] == "р":
    n = rus_alphabet
else:
    n = eng_alphabet
#if step[1] == 'п':
m = input('Напишите какой шаг ')
if m.isdigit():
    m = int(m)
else:
    while not m.isdigit():
        m = input("Напишите целое число!!!: ")
    m = int(m)
    
# функция Шифр цезаря    
def cesar():        
    total = ''  
    if cod[0] == 'ш': #направление шага  
        for c in s:
            if c.isupper() and c.isalpha():
                ind = n.index(c.lower())
                cs = n[(ind + m) % len(n)].upper()
                total += cs
            elif c.islower() and c.isalpha():
                ind = n.index(c)
                cs = n[(ind + m) % len(n)] 
                total += cs
            else:
                total += c 
    else:
        for c in s:
            if c.isupper() and c.isalpha():
                ind = n.index(c.lower())
                cs = n[ind - m].upper()
                total += cs
            elif c.islower() and c.isalpha():
                ind = n.index(c)
                cs = n[ind - m]
                total += cs
            else:
                total += c 
    return total
                
print(cesar())
            
            
            
            
                
            
        
               

    
    
        
    