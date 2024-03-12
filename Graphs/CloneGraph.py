# Using DFS to recursively visit every neighbor of the node and clone them. 
# the visited dictionary stores the cloned copy of the nodes. 
# since the given graph is undirected, it's essential to 

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {} 
        def dfs(node):
            if node.val in visited.keys():
                return visited[node.val]
            clonedNode = Node(node.val)
            visited[node.val] = clonedNode
            clonedNode.neighbors = []
            for neighbor in node.neighbors:
                clonedNode.neighbors.append(dfs(neighbor))
            return clonedNode
        if node:
            return dfs(node)
