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

def remove_node(root,level,k):
    if root is None:
        return(None)

    root.left = remove_node(root.left,level+1,k)
    root.right = remove_node(root.right,level+1,k)
    
    if root.left is None and root.right is None and level < k:
        
        print("-------",level)
        del root
        return(None)

    return(root)
    

    

def main():
    k = 4
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)
    root.right.right = Node(6)
    root.right.right.left = Node(8)

    root.print_tree()
    remove_node(root,1,k)

    print("---------------------")
    root.print_tree()


main()
