# This is an interesting problem. 
# there is a catch 

# slow = nums[0] and fast = nums[nums[0] and doing while slow != fast doesn't work. 
# Not sure why.


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
