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


def Leaf_node(root):
    if root is None:
        return(0)
    if root.left is None and root.right is None:
        return(1)
    return(Leaf_node(root.left) + Leaf_node(root.right))

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    #root.print_tree()
    print(Leaf_node(root))

main()
