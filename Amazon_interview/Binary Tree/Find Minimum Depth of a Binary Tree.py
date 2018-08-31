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


def mini_depth(root):
    if root is None:
        return(0)
    if root.left is None and root.right is None:
        return(1)

    if root.left is None:
        return(mini_depth(root.right)+1)
    if root.right is None:
        return(mini_depth(root.left)+1)

    return((min(mini_depth(root.left),mini_depth(root.right)))+1)
        


def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)

    #root.print_tree()
    print(mini_depth(root)) 


main()
