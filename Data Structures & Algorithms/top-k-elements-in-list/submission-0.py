class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        ans = []
        freq = sorted(freq.items(), key=lambda t: t[1], reverse=True)
        for i in range(k):
            ans.append(freq[i][0])
        return ans
