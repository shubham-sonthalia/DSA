# https://leetcode.com/problems/minimum-falling-path-sum-ii/
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[-1 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[0][i] = grid[0][i]
        
        for i in range(1, n):
            for j in range(n):
                mini = float('inf')
                for k in range(n):
                    if k != j:
                        mini = min(grid[i][j] + dp[i - 1][k], mini)
                dp[i][j] = mini
        return min(dp[n - 1])
