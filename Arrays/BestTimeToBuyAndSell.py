class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0 
        mini = float('inf')
        n = len(prices)
        for i in range(n):
            if prices[i] > mini: 
                maxi = max(maxi, prices[i] - mini)
            else:
                mini = prices[i]
        return maxi
