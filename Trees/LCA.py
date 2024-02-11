class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root.val == p.val or root.val == q.val: 
            return root
        res1 = self.lowestCommonAncestor(root.left, p, q)
        res2 = self.lowestCommonAncestor(root.right, p, q)
        if res1 is not None and res2 is not None:
            return root
        if res1 is None:
            return res2
        if res2 is None:
            return res1
