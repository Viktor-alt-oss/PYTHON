# объявление функции
def is_valid_password(password):
    s = password.split(':')
    s1 = int(s[0])
    s2 = int(s[1])
    s3 = int(s[2])
    counter = 0
    for i in range(2, s2 + 1):
        if s2 % i == 0:
            counter += 1
    if s1[::1] == s1[::-1] and s3 % 2 == 0 and counter == 1:
        return 
            

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))