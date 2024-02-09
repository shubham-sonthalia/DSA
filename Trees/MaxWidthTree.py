class Solution:
    class NodeWithIndex:
        def __init__(self, node, idx):
            self.node = node
            self.idx = idx 
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [] 
        queue.append(self.NodeWithIndex(root, 0))
        maxWidth = 0
        while queue:
            n = len(queue)
            maxWidth = max(queue[-1].idx - queue[0].idx  + 1, maxWidth)
            for i in range(n):
                element = queue.pop(0)
                if element.node.left is not None:
                    queue.append(self.NodeWithIndex(element.node.left, 2*element.idx + 1))
                if element.node.right is not None:
                    queue.append(self.NodeWithIndex(element.node.right, 2*element.idx + 2))
        return maxWidth
