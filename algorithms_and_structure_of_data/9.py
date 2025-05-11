import numpy as np

original_list = np.array([[1, 2, 3], [4, 5, 6]])
copied_list = np.copy(original_list)

original_list[0][0] = 99

print("Оригинальный список:", original_list)  # [[99  2  3] [ 4  5  6]]
print("Скопированный список:", copied_list)  # [[1  2  3] [4  5  6]]