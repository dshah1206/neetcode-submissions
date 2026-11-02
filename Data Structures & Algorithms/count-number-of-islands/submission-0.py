from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        visited = set()

        def bfs(r, c):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    island += 1

        return island

                

        