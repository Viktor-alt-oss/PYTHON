def maxProduct(nums):
    max_prod = min_prod = result = nums[0]
    
    for num in nums[1:]:
        candidates = (num, max_prod * num, min_prod * num)
        min_prod = min(candidates)
        max_prod = max(candidates)
        result = max(result, max_prod)

    return result

nums = [2, 3, -2, 4]
print(maxProduct(nums))