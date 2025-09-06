def closest_to_zero_pair(nums):
    nums = tuple(sorted(nums))   
    pair = (nums[0], nums[1])
    total = sum(pair)
    return pair, total
nums = (10, 2, 5, 30, 12)
pair, total = closest_to_zero_pair(nums)
print("Pair closest to zero:", pair, "with sum:", total)
