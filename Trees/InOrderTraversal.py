class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = [] 
        ans = ans + self.inorderTraversal(root.left)
        ans.append(root.val)
        ans = ans + self.inorderTraversal(root.right)
        return ans
