class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def isMirror(left, right):
            if left is None:
                return right == None
            if right is None:
                return left == None
            if left.val != right.val:
                return False
            res1 = isMirror(left.right, right.left)
            if res1 == True:
                return isMirror(left.left, right.right)
        return isMirror(root.left, root.right)
