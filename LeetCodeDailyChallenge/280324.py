from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # sliding window
        # subarray longest length of the subarray that is "good"
        # frequency of each element <= k 
        n = len(nums)
        i = 0
        j = 0 
        ans = 0 
        hmap = {}
        while j < n:
            if nums[j] in hmap:
                while i < j and not hmap[nums[j]] < k:
                    hmap[nums[i]] -= 1
                    i +=1
                hmap[nums[j]] += 1
            else:
                hmap[nums[j]] = 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans    

                    
        