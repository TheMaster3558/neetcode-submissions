from functools import cache

class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(self.recurse(i, tuple(nums)) for i in range(len(nums)))
    
    @cache
    def recurse(self, i, nums):
        if i >= len(nums):
            return 0
        try:
            return nums[i] + max(self.recurse(j, nums) for j in range(i+2, len(nums)))
        except ValueError as e:
            return nums[i]