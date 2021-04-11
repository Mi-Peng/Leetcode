from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    for i in range(1, m):
        grid[i][0] = grid[i-1][0] + grid[i][0]
    for i in range(1, n):
        grid[0][i] = grid[0][i-1] + grid[0][i]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = min([grid[i-1][j], grid[i][j-1]]) + grid[i][j]
    return grid[-1][-1]


grid = [[1,2,3],
       [4,5,6]]
# ans=12
print(minPathSum(grid))