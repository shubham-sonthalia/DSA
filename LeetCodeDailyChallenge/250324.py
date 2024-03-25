# use the range of nums[i] to your advantage
# for each nums[i], find the absolute value, and then check if the nums[x - 1] is negative.
# If yes, then it's already present. So we can add it to the output.



class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = [] 
        for num in nums:
            x = abs(num)
            if nums[x - 1] < 0:
                output.append(x)
            nums[x - 1] *= -1
        return output
