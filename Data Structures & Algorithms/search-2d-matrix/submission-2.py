class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix)-1
        row = None
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = matrix[mid]
                break
            elif matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        if row is None:
            return False

        lo, hi = 0, len(row)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
        
