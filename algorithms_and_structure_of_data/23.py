def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = len(arr) // 2
    left = [x for x in arr if x < arr[pivot]]
    mid = [x for x in arr if x == arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]

    return quick_sort(left) + mid + quick_sort(right)

array = [10, 7, 8, 9, 1, 5]
sorted_array = quick_sort(array)
print("Отсортированный массив:", sorted_array)
