class Node:
    mini_depth = 234556
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

def mini_depth(root,count):
    if root is None:
        return
    print("mini_depth= %d , depth= %d"%(Node.mini_depth,count))
    if root.left is None:
        if Node.mini_depth > count:
            Node.mini_depth = count
    if root.right is None:
        if Node.mini_depth < count:
            Node.mini_depth = count
            
    mini_depth(root.left,count+1)
    mini_depth(root.right,count+1)
        




def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.left.left = Node(6)
    root.left.left.right = Node(7)
    root.right = Node(3)
    root.right.left = Node(8)
    root.right.right = Node(9)

    #root.print_tree()
    mini_depth(root,0)
    print(Node.mini_depth)

main()
