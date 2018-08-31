class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,value):
        if self.data is not None:
            if self.data > value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif self.data < value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)


        else:
            self.data = Node(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def height(self,root):
        if root is None:
            return(True)
        return(max(self.height(root.left),self.height(root.right))+1)

    def isBalanced(self,root):
        if root is None:
            return(True)

        lh = self.height(root.left)
        rh = self.height(root.right)

        if ((abs(lh-rh) >= 1) and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True):
            return(True)
        return(False)

def main():
    elements = list(map(int,input("Please enter the elements: ").split()))
    for i in range(len(elements)):
        if i == 0:
            root = Node(elements[i])
        else:
            root.insert(elements[i])
    root.print_tree()
    if root.isBalanced(root) == True:
        print("True")
    else:
        print("False")


main()
