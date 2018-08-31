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


def add(root):
    if root is None:
        return(False)
    return(add(root.left) + root.data + add(root.right))

def Sum_tree(root):
    if root is None:
        return(True)
    if root.left is None and root.right is None:
        return(True)

    add_left = add(root.left)
    add_right = add(root.right)

    total = add_left + add_right
    if (root.data == total):
        return (Sum_tree(root.left) and Sum_tree(root.right))
        

def main():
    root = Node(26)
    root.left = Node(10)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(6)

    #root.print_tree()
    print(Sum_tree(root))


main()
