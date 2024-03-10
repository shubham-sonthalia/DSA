class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = float('-inf')
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s > curMax:
                curMax = s
            if s < 0:
                s = 0
        return curMax
