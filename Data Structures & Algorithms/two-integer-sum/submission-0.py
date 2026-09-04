class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {target - nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] in previous:
                return [previous[nums[i]], i]
            previous[target - nums[i]] = i
            
