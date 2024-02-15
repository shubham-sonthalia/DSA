class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = {} 
        for idx, num in enumerate(inorder):
            d[num] = idx 
        def create(postStart, postEnd, inStart, inEnd, d):
            if postStart > postEnd or inStart > inEnd: 
                return None
            curRootVal = postorder[postEnd]
            curRoot = TreeNode(curRootVal)
            inOrderIdx = d[curRootVal]
            lenOfLeftSubtree = inOrderIdx - inStart
            curRoot.left = create(postStart, postStart + lenOfLeftSubtree - 1, inStart, inOrderIdx - 1, d)
            curRoot.right = create(postStart + lenOfLeftSubtree, postEnd - 1, inOrderIdx + 1, inEnd, d)
            return curRoot
        return create(0, len(postorder) - 1, 0, len(inorder) - 1, d)
