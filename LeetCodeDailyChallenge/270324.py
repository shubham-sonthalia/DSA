#Sliding Window Concept 
#O(n)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #Initialization
        i = 0
        j = 0 
        n = len(nums)
        p = 1
        ans = 0
        while j < n:
            p *= nums[j]
            while i < j and p >= k:
                p = p//nums[i]
                i += 1
            if p < k:
                ans += j - i + 1
            j += 1
        return ans
