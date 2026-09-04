class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        answer = 0

        for right in range(1, len(prices)):
            while left < right and prices[left] >= prices[right]:
                left += 1
            answer = max(answer, prices[right] - prices[left])

        return answer

        