for i in range(1, 33):
    for j in range(1, 33):
        for k in range(1, 33):
            for f in range(1,33):
                if i ** 3 + j ** 3 == k ** 3 + f ** 3:
                    print(i, j, k, f)
            