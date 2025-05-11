def two_sum(nums, target):
    dict_nums = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in dict_nums:
            return sorted([i, dict_nums[complement]])
        dict_nums[num] = i

nums = [2, 11, 7, 15]
target = 9
print(two_sum(nums, target)) 