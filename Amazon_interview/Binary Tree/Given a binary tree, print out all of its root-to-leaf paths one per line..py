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

def root_to_leaf(root,path,i):
    if root is None:
        return
    else:
        path[i] = root.data
        i += 1
        if root.left is None and root.right is None:
            print(path[:i],i)
        else:
            root_to_leaf(root.left,path,i)
            root_to_leaf(root.right,path,i)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    path = [0] * 100
    root.print_tree()
    root_to_leaf(root,path,0)
    
main()
