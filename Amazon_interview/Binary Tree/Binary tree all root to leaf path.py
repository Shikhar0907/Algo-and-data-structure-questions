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

def printPath(root,path,pathlen):
    if root is None:
        return
    if len(path) == 0:
        path.append(root.data)
    

    pathlen += 1
    if root.left is None and root.right is None:
        printArray(path,pathlen)

    else:
        printPath(root.left,path,pathlen)
        printPath(root.right,path,pathlen)


def printArray(arr,pathlen):
    for i in arr:
        print(i)

def main():
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right = Node(2)
    root.right.left = Node(2)
    #root.print_tree()
    path = []
    printPath(root,path,0)
    

main()
