import bisect

def lengthOfLIS(nums):
    tails = []
    for num in nums:
        idx = bisect.bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return tails

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums)) 
