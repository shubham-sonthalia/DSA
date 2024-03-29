class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = len(nums)
        i = 0 
        j = 0
        count = 0
        res = 0 
        while j < n:
            if nums[j] == m:
                count += 1  
            if count >= k:
                while count > k or (i <= j and nums[i] != m and count == k):
                    if nums[i] == m:
                        count -= 1
                    i += 1
                res += i + 1   
            j += 1
        return res
