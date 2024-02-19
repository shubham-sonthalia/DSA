class Solution:
    def kthLargest(self,root, k):
        def cal(root):
            if not root:
                return []
            ans = [] 
            if root.left:
                ans += cal(root.left)
            ans.append(root.data)
            if root.right:
                ans += cal(root.right)
            return ans
        inorder = cal(root)
        return inorder[len(inorder) - 1 - (k - 1)]
