class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(low, high):
            if low > high: 
                return None
            mid = low + (high - low)//2 
            root = TreeNode(nums[mid])
            root.left = convert(low, mid - 1)
            root.right = convert(mid + 1, high)
            return root
        return convert(0, len(nums) - 1)
