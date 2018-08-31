class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:

            self.right.print_tree()

def isFullTree(root):
    if root is None:
        return(True)

    if root.left is None and root.right is None:
        return(True)

    if root.left is not None and root.right is not None:
        return(isFullTree(root.left) and isFullTree(root.right))

def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)

    #root.print_tree()
    print(isFullTree(root))


main()
