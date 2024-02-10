class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(root):
            if not root:
                return -1
            left = right = -1
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)
            ans[0] = max(ans[0], left + right  + 2)
            return 1 + max(left, right)
        dfs(root)
        return ans[0]
