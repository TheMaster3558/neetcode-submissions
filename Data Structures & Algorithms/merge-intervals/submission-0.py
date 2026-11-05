class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            a, b = intervals[i]
            if merged[-1][1] >= a:
                merged[-1][1] = max(merged[-1][1], b)
            else:
                merged.append(intervals[i])

        return merged