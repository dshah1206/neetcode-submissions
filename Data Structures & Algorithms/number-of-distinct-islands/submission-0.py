class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        unique_island = set()
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or not grid[r][c] or (r,c) in visited:
                return
            visited.add((r,c))
            current_island.add((r-row_og,c-col_og))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for i in range(m):
            for j in range(n):
                row_og = i
                col_og = j
                current_island = set()
                dfs(i,j)
                if current_island:
                    unique_island.add(frozenset(current_island))
        
        return len(unique_island)


        
        