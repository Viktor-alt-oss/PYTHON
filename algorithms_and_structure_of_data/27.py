def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid +1
        else:
            right = mid

    return left

arr = [1, 3, 20, 4, 1, 0, 10, 8]
local_max = findPeakElement(arr)
print(f"Локальный максимум: {local_max}")