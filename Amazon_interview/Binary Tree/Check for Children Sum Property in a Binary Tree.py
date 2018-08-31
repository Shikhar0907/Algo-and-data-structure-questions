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


def isSumProperty(root):
    left_data = 0
    right_data = 0
    if root is None or (root.left is None and root.right is None):
        return(True)
    else:
        if root.left is not None:
            left_data = root.left.data
        if root.right is not None:
            right_data = root.right.data

        if root.data == left_data + right_data and isSumProperty(root.left) and isSumProperty(root.right):
            return(True)
        else:
            return(False)

def main():
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right = Node(2)
    root.right.left = Node(2)

    root.print_tree()
    print(isSumProperty(root))

main()
