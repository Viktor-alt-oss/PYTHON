height = 8
widht = 15
for i in range(1, height + 1):
    for j in range(('' * (widht - i)) + ('*' * i)):
        print(j) 