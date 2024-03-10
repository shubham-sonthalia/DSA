class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find i such that nums[i] < nums[i + 1]
        # swap nums[i] with the first number that is greater than nums[i]
        # from the end
        # swap nums[firstGreaterElementFromEnd] with nums[i]
        # reverse the array from i + 1 to n - 1
        def swapElements(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp 
        def reverseArray(start, end):
            l = end - start + 1
            for i in range(l//2):
                swapElements(start + i, end - i)
        def findFirstGreaterElementFromEnd(idx):
            n = len(nums)
            for i in range(n - 1, idx, -1):
                if nums[i] > nums[idx]:
                    return i    
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                swapElements(i, findFirstGreaterElementFromEnd(i))
                reverseArray(i + 1, len(nums) - 1)
                break
            else:
                if i == 0:
                    reverseArray(0, len(nums) - 1)
                    break
