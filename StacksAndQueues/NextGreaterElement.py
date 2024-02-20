# Brute Force Approach
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        d = {} 
        for idx, nums in enumerate(nums2):
            d[nums] = idx
        for n in nums1:
            idx = d[n]
            added = False
            for i in range(idx + 1, len(nums2)):
                if nums2[idx] < nums2[i]:
                    added = True
                    ans.append(nums2[i])
                    break
            if not added:
                ans.append(-1)
        return ans
