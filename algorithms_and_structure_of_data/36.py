def single_number(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

nums = [4, 1, 2, 1, 2]
print(single_number(nums))