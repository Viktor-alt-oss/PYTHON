# объявление функции
text = 'TheThe'
total = ''
for s in range(len(text)):
    if s.isupper():
        total += '_' + s
    else:
        total += s
print(total)        
    
            
        
