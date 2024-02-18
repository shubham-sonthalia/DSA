def floorInBST(root, X):
    if root is None:
        return -1 
    if root.data <= X: 
        if root.right: 
            return max(root.data, floorInBST(root.right, X))
        return root.data 
    if root.data > X: 
        if root.left:
            return floorInBST(root.left, X)
        return -1 
