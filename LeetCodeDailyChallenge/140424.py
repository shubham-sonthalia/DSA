# https://leetcode.com/problems/sum-of-left-leaves/?envType=daily-question&envId=2024-04-14
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isRoot = True) -> int:
        if not root: 
            return 0
        queue = []
        queue.append((root, False))
        s = 0 
        while queue:
            cur = queue.pop(0)
            if cur[1]:
                if not cur[0].left and not cur[0].right:
                    s += cur[0].val
            if cur[0].left:
                queue.append((cur[0].left, True))
            if cur[0].right:
                queue.append((cur[0].right, False))
        return s
