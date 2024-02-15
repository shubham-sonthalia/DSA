class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d =  {} 
        for idx, num in enumerate(inorder):
            d[num] = idx
        def create(preStart, preEnd, inStart, inEnd, d):
            if preStart > preEnd or inStart > inEnd:
                return None
            curRootVal = preorder[preStart]
            curRoot = TreeNode(curRootVal)
            inPosIdx = d[curRootVal]
            lenOfLeftHalf = inPosIdx  - inStart
            curRoot.left = create(preStart + 1, preStart + lenOfLeftHalf, inStart, inPosIdx - 1, d)
            curRoot.right = create(preStart + lenOfLeftHalf + 1 , preEnd, inPosIdx + 1, inEnd, d)
            return curRoot
        return create(0, len(preorder) - 1, 0, len(inorder) - 1, d)
