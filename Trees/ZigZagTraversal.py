class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [] 
        level = 0 
        ans = []
        if root is not None:
            queue.append(root)
        while queue:
            n = len(queue)
            arr = [] 
            for i in range(n):
                cur = queue.pop(0)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                arr.append(cur.val)
            if level % 2 == 0:
                ans.append(arr)
            else:
                ans.append(arr[::-1])
            level += 1
        return ans  
