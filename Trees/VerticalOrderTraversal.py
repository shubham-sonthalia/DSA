class Solution:
    class spclNode: 
        def __init__(self, node, x, y):
            self.node = node
            self.x = x
            self.y = y
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [] 
        queue.append(self.spclNode(root, 0, 0))
        d = {} 
        while queue:
            element = queue.pop(0)
            if element.y in d:
                d[element.y].append((element.x, element.node.val))
            else:
                d[element.y] = [(element.x, element.node.val)]
            if element.node.left is not None:
                queue.append(self.spclNode(element.node.left, element.x + 1, element.y - 1))
            if element.node.right is not None:
                queue.append(self.spclNode(element.node.right, element.x + 1, element.y + 1))
        ans = []
        l = list(d.items())
        l.sort(key = lambda x: x[0])
        for k, value in l:         
            value.sort(key = lambda x: x[1])
            value.sort(key = lambda x: x[0]) 
            arr = [] 
            for x, val in value: 
                arr.append(val)
            ans.append(arr)
        return ans   
