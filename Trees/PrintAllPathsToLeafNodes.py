def allRootToLeaf(root) -> List[str]:
    # Base Condition 
    def recursion(root, cur):
        if cur == "":
            cur += str(root.data)
        else:
            cur += " " + str(root.data)
        if root.left is None and root.right is None:
            return [cur]
        ans = [] 
        if root.left is not None: 
            ans += recursion(root.left, cur)
        if root.right is not None:
            ans += recursion(root.right, cur)
        return ans 
    return recursion(root, "")
