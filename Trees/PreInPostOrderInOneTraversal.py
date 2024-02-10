class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
class Pair:
    def __init__(self, node, num):
        self.node = node
        self.num = num
def getTreeTraversal(root):
    # Write your code here.
    inorder = [] 
    preorder = [] 
    postorder = [] 
    stackList = []
    stackList.append(Pair(root, 1))
    while stackList:
        cur = stackList.pop()
        if cur.num == 1:
            preorder.append(cur.node.data)
            stackList.append(Pair(cur.node, 2))
            if cur.node.left is not None:
                stackList.append(Pair(cur.node.left, 1))
        if cur.num == 2: 
            inorder.append(cur.node.data)
            stackList.append(Pair(cur.node, 3))
            if cur.node.right is not None:
                stackList.append(Pair(cur.node.right, 1))
        if cur.num == 3:
            postorder.append(cur.node.data)
    return [inorder, preorder, postorder]
