class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder traversal 
        def cal(root):
            ans = [] 
            if not root:
                return
            if root.left:
                ans += cal(root.left)
            ans.append(root.val)
            if root.right:
                ans += cal(root.right)
            return ans
        
        inorder = cal(root)
        if k <= len(inorder):
            return inorder[k - 1]
        return -1
