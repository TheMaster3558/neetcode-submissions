from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost = tuple(cost)
        return min(self.recurse(len(cost)-1, cost), self.recurse(len(cost)-2, cost))

    @cache
    def recurse(self, i, cost):
        if i == 0:
            return cost[0]
        if i == 1:
            return cost[1]
        return cost[i] + min(self.recurse(i-1, cost), self.recurse(i-2, cost))
        