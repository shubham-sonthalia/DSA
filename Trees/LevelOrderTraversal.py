class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [] 
        ans = []
        if root is not None:
            queue.append(root)
        while queue:
            length = len(queue)
            arr = []
            for i in range(length):
                cur = queue.pop(0)
                if cur.left is not None:
                    queue.append(cur.left)
                if cur.right is not None:
                    queue.append(cur.right)
                arr.append(cur.val)
            ans.append(arr)
        return ans
