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

def difference(root):
    if root is None:
        return(0)
    return(root.data - difference(root.left) - difference(root.right))


def main():
    root = Node(5)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.left.right.left = Node(3)
    root.right = Node(6)
    root.right.right = Node(8)
    root.right.right.left = Node(7)
    root.right.right.right = Node(9)

    #root.print_tree()
    print(difference(root))


main()
