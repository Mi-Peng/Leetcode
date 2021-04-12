from typing import List

# dp
def minPathSum(matrix: List[List[int]]) -> int:
    r = len(matrix)
    c = len(matrix[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0] = matrix[0][0]
    for ci in range(1, c):
        dp[0][ci] = dp[0][ci - 1] + matrix[0][ci]
    for ri in range(1, r):
        dp[ri][0] = dp[ri - 1][0] + matrix[ri][0]
    for i in range(1, r):
        for j in range(1, c):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    return dp[-1][-1]


grid = [[1,2,3],
       [4,5,6]]
# ans=12
print(minPathSum(grid))