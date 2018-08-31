mini = -2345
maxi = 2342

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

def isBST(root,mini,maxi):
    if root is None:
        return(True)
    #print(root.data,mini,maxi)
    if root.data < mini or root.data > maxi:
        
        return(False)
    return(isBST(root.left,mini,root.data) and isBST(root.right,root.data,maxi))
    

def main():
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(10)
    root.left.right = Node(4)
    root.right = Node(8)
    root.right.left = Node(7)
    root.right.right = Node(9)

    #root.print_tree()
    print(isBST(root,mini,maxi))

main()
