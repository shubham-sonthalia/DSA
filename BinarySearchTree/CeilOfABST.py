
def findCeil(root, x):
    ceil = -1 
    while (root):
        if root.data == x:
            ceil = root.data
            return ceil 
        elif root.data > x: 
            ceil = root.data
            root = root.left 
        elif root.data < x:
            root = root.right 
    return ceil
