class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*m for _ in range(n)]
        for i in range(m):
            grid[0][i] = 1
        for i in range(n):
            grid[i][0] = 1
        for y in range(1,n):
            for x in range(1,m):
                grid[y][x] = grid[y-1][x] + grid[y][x-1]
        return grid[-1][-1]
