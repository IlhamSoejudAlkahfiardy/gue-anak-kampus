class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.center = None
        self.right = None
def maxDepth(node):
    if node is None:
        return -1;
    else:
        lDepth = maxDepth(node.left)
        cDepth = maxDepth(node.center)
        rDepth = maxDepth(node.right)

        if(lDepth > cDepth):
            return lDepth +1
        elif (cDepth > rDepth):
            return cDepth +1
        else:
            return rDepth +1

root = Node(0)
root.left = Node(2)
root.center = Node(1)
root.right = Node(5)
root.left.center = Node(3)
root.right.left = Node(4)
root.right.right = Node(6)

print("Height of tree is %d" %(maxDepth(root)))
