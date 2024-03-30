#for exactly k distinct integers in a subarray, the idea is to find the atmost k distinct integers in the subarray
# and subtract the number with atmost k - 1 distinct integers in the subarray. 

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #atmost k - atmost k - 1
        def countOfSubArraysWithAtmostKDistinct(nums, k):
            i = 0
            j = 0 
            n = len(nums)
            res = 0
            hmap = {}
            while j < n:
                if nums[j] not in hmap:
                    hmap[nums[j]] = 1
                else:
                    hmap[nums[j]] += 1
                while len(hmap) > k:
                    hmap[nums[i]] -= 1
                    if hmap[nums[i]] == 0:
                        del hmap[nums[i]]
                    i += 1
                if len(hmap) <= k:
                    res += j - i + 1
                j += 1
            return res
        return countOfSubArraysWithAtmostKDistinct(nums, k) - countOfSubArraysWithAtmostKDistinct(nums, k - 1)
        


        
