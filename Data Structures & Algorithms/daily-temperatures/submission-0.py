class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0, temperatures[0])]
        ans = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                index, temp = stack.pop()
                ans[index] = i - index
            stack.append((i, temperatures[i]))
        return ans
        