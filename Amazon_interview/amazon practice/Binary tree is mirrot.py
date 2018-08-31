class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isMirror(root,start):
    if root is None and start is None:
        return(True)
    if root is None or start is None:
        return(False)

    if root.data == start.data:
        return(isMirror(root.left,start.right) and isMirror(root.right,start.left))

def main():
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(4)


    start = Node(1)
    start.left = Node(2)
    start.left.left = Node(4)
    start.left.right = Node(5)
    start.right = Node(3)

    if isMirror(root,start) == True:
        print('Yes')
    else:
        print("False")

    
main()     
