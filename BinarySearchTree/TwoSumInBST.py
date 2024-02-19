# Inorder approach

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def cal(root):
            if not root:
                return []
            ans = [] 
            if root.left:
                ans += cal(root.left)
            ans.append(root.val)
            if root.right:
                ans += cal(root.right)
            return ans
        inorder = cal(root)
        i = 0
        j = len(inorder) - 1
        res = False
        while i < j:
            if inorder[i] + inorder[j] < k:
                i += 1
            elif inorder[i] + inorder[j] == k:
                return True 
            else:
                j -= 1
        return res
#Optimal Soln
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = [] 
        used = set() 
        if root: 
            q.append(root)
        while q:
            cur = q.pop(0)
            if k - cur.val in used:
                return True 
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            used.add(cur.val)   
        return False
