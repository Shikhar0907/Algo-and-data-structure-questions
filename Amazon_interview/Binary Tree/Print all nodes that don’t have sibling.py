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

def No_sibling(root):
    if root is None:
        return
    if root.left is not None and root.right is not None:
        No_sibling(root.left)
        No_sibling(root.right)
    elif root.left is not None:
        print(root.left.data)
        No_sibling(root.left)

    elif root.right is not None:
        print(root.right.data)
        No_sibling(root.right)
        

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.left.left = Node(6)

    #root.print_tree()
    No_sibling(root)

main()
