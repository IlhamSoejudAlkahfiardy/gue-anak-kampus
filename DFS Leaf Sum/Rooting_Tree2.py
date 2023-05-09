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

        if(lDepth > cDepth or lDepth > rDepth):
            return lDepth +1
        elif (cDepth > lDepth or cDepth > rDepth):
            return cDepth +1
        else:
            return rDepth +1

root = Node(5)
root.left = Node(0)
root.center = Node(4)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)
root.left.right.right = Node(3)
root.left.right.left = Node(3)


print("Height of tree is %d" %(maxDepth(root)))
