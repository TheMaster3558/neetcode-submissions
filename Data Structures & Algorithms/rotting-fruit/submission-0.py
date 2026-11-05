from collections import deque
import math
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rotton = []
        oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotton.append((i, j))
                if grid[i][j] != 0:
                    oranges += 1

        q = deque()
        for i, j in rotton:
            q.append((i, j, 0))

        visited = set()
        longest_mins = 0
        while q:
            i, j, t = q.popleft()
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or (i, j) in visited or grid[i][j] == 0:
                continue
            visited.add((i, j))
         
            if grid[i][j] == 1:
                longest_mins = max(longest_mins, t)
            q.append((i+1, j, t+1))   
            q.append((i-1, j, t+1))
            q.append((i, j+1, t+1))
            q.append((i, j-1, t+1))

        if len(visited) != oranges:
            return -1

        return longest_mins
            
