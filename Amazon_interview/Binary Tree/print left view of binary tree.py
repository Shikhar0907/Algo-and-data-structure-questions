class Node:
    max_level = 0
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.max_level = None
        

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

def left_view(root,level,length):
    if root is None:
        return
    Node.max_level = length
    print("level = %d, max_level = %d"%(level,Node.max_level))
    if Node.max_level < level:
        print(root.data)
        Node.max_level = level
        
    
    left_view(root.left,level+1,Node.max_level)
    left_view(root.right,level+1,Node.max_level)
    
    
        

def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(6)
    root.right.left = Node(10)
    #root.print_tree()

    
    print(Node.max_level)
    left_view(root,1,Node.max_level)

main()
