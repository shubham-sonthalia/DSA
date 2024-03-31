# revisit

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        badi = -1
        mini = -1
        maxi = -1
        n = len(nums)

        for i in range(n):
            if nums[i] > maxK or nums[i] < minK:
                badi = i
            if nums[i] == minK:
                mini = i
            if nums[i] == maxK:
                maxi = i
            ans += max(0, min(maxi, mini) - badi)
        return ans
