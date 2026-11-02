from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        def out_of_bounds(r, c):
            return (r>=n or c>=n or r<0 or c<0)

        def dfs(r,c,label):
            """ Calculate area of islands and flip the label """
            stack = [(r, c)]
            grid[r][c] = label
            size = 0
            while stack:
                curr_r, curr_c = stack.pop()
                size += 1
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    if not out_of_bounds(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = label
                        stack.append((nr, nc))
            return size

        size = defaultdict(int)
        label = 2

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    size[label] = dfs(r,c,label)
                    label += 1

        def connect(r, c):
            """ Flipping the water to land and checking the max area """
            visited = set()
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not out_of_bounds(nr, nc) and grid[nr][nc] not in visited:
                    res += size[grid[nr][nc]]
                    visited.add(grid[nr][nc])
            return res           

        area = 0 if not size else max(size.values())
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    area = max(area, connect(r,c))
        return area
