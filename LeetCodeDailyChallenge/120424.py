# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        preMax = [0 for i in range(n)]
        suffMax = [0 for i in range(n)]
        
        preMax[0] = height[0]
        suffMax[-1] = height[-1]

        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            suffMax[i] = max(suffMax[i + 1], height[i])
        
        res = 0 

        for i in range(n):
            res += min(preMax[i], suffMax[i]) - height[i]

        return res
