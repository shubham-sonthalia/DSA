class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        ans.append(root.val)
        ans += self.preorderTraversal(root.left)
        ans += self.preorderTraversal(root.right)
        return ans   
