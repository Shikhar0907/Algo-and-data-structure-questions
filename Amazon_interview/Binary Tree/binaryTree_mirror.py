class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def areMirror(root,start):
    if root is None and start is None:
        return(True)
    if root is None or start is None:
        return(False)
    
    if root is not None and start is not None:
        if root.data == start.data:
            return(areMirror(root.left,start.right) and areMirror(root.right,start.left))
    
def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)

    start = BinaryTree(1)
    start.left = BinaryTree(3)
    start.right = BinaryTree(2)
    start.right.left = BinaryTree(5)
    start.right.right = BinaryTree(4)

    if areMirror(root,start) == True:
        print("Yes")
    else:
        print("No")


main()
