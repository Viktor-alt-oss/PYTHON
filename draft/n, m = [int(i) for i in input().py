n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
template = sorted([(i + j, i, j) for i in range(n) for j in range(m)])
for id, item in enumerate(template): 
    matrix[item][item] = id + 1
[print(*[str(item).ljust(3) for item in row]) for row in matrix]