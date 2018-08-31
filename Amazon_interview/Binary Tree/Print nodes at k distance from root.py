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

def distance(root,num):
    if root is None:
        return(False)
    
    dist = distance(root.left,num)
    dist = distance(root.right,num)
    if root.data == num:
        return(True)
    return(dist+1)
       

def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(8)

    #root.print_tree()
    num = 4
    dist = 0
    print(distance(root,num))


main()
