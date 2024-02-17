# O(n2)
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def cal(preStart, preEnd):
            if preStart > preEnd:
                return None
            rootVal = preorder[preStart]
            root = TreeNode(rootVal)
            idxOfGreaterElement = preEnd + 1
            for i in range(preStart + 1, preEnd + 1):
                if preorder[i] > preorder[preStart]:
                    idxOfGreaterElement = i 
                    break
            root.left = cal(preStart + 1, idxOfGreaterElement - 1)
            root.right = cal(idxOfGreaterElement, preEnd)
            return root
        return cal(0, len(preorder) - 1)   

# O(n) Stack Implementation. Same intuition as Next Greater Element problem

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        stack = [root]
        for i in range(1, len(preorder)):
            newNode = TreeNode(preorder[i])
            cur = None
            while stack and stack[-1].val < preorder[i]:
                cur = stack.pop(-1)
            if stack and not cur: 
                stack[-1].left = newNode
            elif cur:
                cur.right = newNode
            stack.append(newNode)
        return root   
