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


def mirror(root):
    if root is None:
        return
    mirror(root.left)
    mirror(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

    
    

def main():
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(4)

    root.print_tree()
    mirror(root)
    print("--------------------------------")
    root.print_tree()

main()
