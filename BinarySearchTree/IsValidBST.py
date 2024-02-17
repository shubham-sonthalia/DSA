class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini = float('-inf')
        maxi = float('inf')
        def check(root, mini, maxi):
            if root is None:
                return True
            if root.val > mini and root.val < maxi:
                if check(root.left, mini, root.val):
                    return check(root.right, root.val, maxi)
            return False
        return check(root, mini, maxi)
