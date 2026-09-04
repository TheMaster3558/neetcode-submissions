import math

def sim(piles, h, k):
    hours = 0
    for pile in piles:
        hours += int(math.ceil(pile / k))
    return hours <= h

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if sim(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
        
        