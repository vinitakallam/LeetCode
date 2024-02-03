# Problem: Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.

# Solution: 
from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target: 
                    return [i, j]
        return []

test = Solution()
nums = [2,7,11,15]
target = 9
result = test.twoSum(nums, target)
print(result)
