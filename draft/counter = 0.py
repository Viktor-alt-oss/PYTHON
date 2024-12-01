counter = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1

print("Было введено", counter, "чисел, больших 10.")
