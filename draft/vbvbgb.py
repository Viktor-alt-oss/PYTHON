# put your python code here
s = int(input())
li = [input() for _ in range(s)] # [aaa, vvvv, ddddd]
one = 0
for i in li:
    hacker = ['a', 'n', 't', 'o', 'n', None]
    counter = 0
    for j in range(len(i)):
        if i[j] == hacker[j]:
            counter += 1
            del hacker[j]
            hacker.insert(0, 'z')
            if counter == 5:
                one += 1
        else:
            hacker.insert(0, 'z')

            
print(one)