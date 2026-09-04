class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # divide the product of all nums by current num
        # [1, 2, 3, 4] total product = 1*2*3*4 = 24
        # [24, 12, 8, 6]
        # what if there's a 0, if there's 2 zeroes then everything is 0
        # [0, 1, 2, 3] total_product = 0
        # if there's one zero, then everything is zero, except for the
        # index the zero is at, then its the product of everything but the zero
        num_zeroes = 0
        total_product = 1
        total_product_excluding_zero = 1

        for num in nums:
            if num == 0:
                num_zeroes += 1
            else:
                total_product_excluding_zero *= num
            total_product *= num

        if num_zeroes > 1:
            return [0] * len(nums)

        ans = []
        for num in nums:
            if num == 0:
                ans.append(total_product_excluding_zero)
            elif num_zeroes == 1:
                ans.append(0)
            else:
                ans.append(total_product // num)
        return ans
        