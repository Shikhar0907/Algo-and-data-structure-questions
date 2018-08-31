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

def find_path(root,path,num):

    if root is None:
        return(False)
    
    
    if root.data == num:
        return(True)
    path.append(root.data)
    if (root.left is not None and find_path(root.left,path,num)) or (root.right is not None and find_path(root.right,path,num)):
        return(True)
    
    path.pop()
    return(False)        

def Find_LCA(root,num1,num2):
    path1 = []
    path2 = []

    if (not find_path(root,path1,num1) or not find_path(root,path2,num2)):
        return(-1)

    print(path1)
    print(path2)
    for i in range(len(path1)-1,-1,-1):
        if path1[i] in path2:
            return(path1[i])
    return(-1)
     

def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.print_tree()

    print("{}".format(Find_LCA(root,4,5)))


main()
