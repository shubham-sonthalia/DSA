class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def preorder(root):
            if root is None:
                return []
            ans = [] 
            ans.append(root.val)
            ans += preorder(root.left)
            ans += preorder(root.right)
            return ans
        ans = preorder(root)
        cur = root
        for i in range(1, len(ans)):
            cur.right = TreeNode(ans[i])
            cur.left = None
            cur = cur.right
        return root
