class Solution:
    class NodeWithIndex:
        def __init__(self, node, idx):
            self.node = node
            self.idx = idx 
    def bottomView(self, root):
        d = {} 
        queue = [] 
        queue.append(self.NodeWithIndex(root, 0))
        while queue: 
            element = queue.pop(0)
            d[element.idx] = element.node.data;
            if element.node.left is not None:
                queue.append(self.NodeWithIndex(element.node.left, element.idx - 1))
            if element.node.right is not None:
                queue.append(self.NodeWithIndex(element.node.right, element.idx + 1))
        l = list(d.items())
        l.sort(key = lambda x: x[0])
        ans = [] 
        for a, b in l:
            ans.append(b)
        return ans
