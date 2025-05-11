def shift_array_right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

array = [1, 2, 3, 4, 5]
k = 2
shifted_array = shift_array_right(array, k)
print(shifted_array)
    