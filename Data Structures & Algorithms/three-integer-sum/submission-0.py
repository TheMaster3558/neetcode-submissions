class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                if j == i:
                    j += 1
                elif k == i:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return list(map(list, ans))

        
