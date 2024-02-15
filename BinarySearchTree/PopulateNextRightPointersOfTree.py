
# https://www.codingninjas.com/studio/problems/985347?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

def connectNodes(root):
    # Write your code here.
    queue = [] 
    if root:
        queue.append(root)
    while queue:
        l = len(queue)
        for i in range(l):
            cur = queue.pop(0)
            if queue and i < l - 1:
                cur.next = queue[0]
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    return root
