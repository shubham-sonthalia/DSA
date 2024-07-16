# The shortest path between any two given nodes in a Binary Tree will pass via their LCA
# So we use DFS to find the path between LCA node and the startNode
# Then same approach to find the path between LCA node and the destNode
# Now, whatever is the path stored in the pathFromLCAToSource, we can replace them with "U" because we will have to go up to the 
# LCA and then starting moving towards the destNode. 
# So we do that. And then we append whatever path is there for pathFromLCAToDest to the pathFromLCAToSource list. 


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findLCA(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            
            res1 = findLCA(root.left, p, q)
            res2 = findLCA(root.right, p, q)

            if res1 is not None and res2 is not None:
                return root
            if res1 is None:
                return res2
            if res2 is None:
                return res1
        
        def findPathFromRoot(root, val, s):
            if root is None:
                return False
            if root.val == val:
                return True
            s.append("R")
            if findPathFromRoot(root.right, val, s):
                return True
            s.pop()
            s.append("L")
            if findPathFromRoot(root.left, val, s):
                return True
            s.pop()
            return False
        root = findLCA(root, startValue, destValue)
        pathToSource = []
        pathToDest = []
        findPathFromRoot(root, startValue, pathToSource)
        findPathFromRoot(root, destValue, pathToDest)
        for i in range(len(pathToSource)):
            pathToSource[i] = "U"
        for j in range(len(pathToDest)):
            pathToSource.append(pathToDest[j])
        return "".join(pathToSource)
