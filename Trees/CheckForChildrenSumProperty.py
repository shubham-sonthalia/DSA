def isParentSum(root):
    if not root:
        return True
    s = 0
    if root.left:
        s += root.left.data
    if root.right:
        s += root.right.data
    if s == 0 or s == root.data:
        return True and isParentSum(root.left) and isParentSum(root.right)
    return False    
    # Write your code here.
    pass
