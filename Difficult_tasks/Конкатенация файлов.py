# На вход программе подается натуральное число 𝑛 и n строк с названиями файлов. 
# Напишите программу, которая создает файл output.txt и выводит в него содержимое всех файлов, не меняя их порядка. 

with open('output.txt', 'w', encoding='utf-8') as out:
    for _ in range(int(input())):
        with open(input()) as file:
            out.write(file.read())