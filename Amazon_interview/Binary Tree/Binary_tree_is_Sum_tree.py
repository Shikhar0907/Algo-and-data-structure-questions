leftsum = 0
rigthsum = 0
class BinarySearchTree:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

def add(root):
    if root == None:
        return(0)
    return(add(root.left) + root.data + add(root.right))

def isSumTree(root):
    if root is None:
        return(1)
    if root.left == None and root.right == None:
        return(1)
    
    leftsum = add(root.left)
    rightsum = add(root.right)
    total = leftsum + rightsum
    if root.data == total:
        if isSumTree(root.left) and isSumTree(root.right):
            return(1)
        return(0)
        
def main():
    root = BinarySearchTree(26)
    root.left = BinarySearchTree(10)
    root.right = BinarySearchTree(3)
    root.left.left = BinarySearchTree(4)
    root.left.right = BinarySearchTree(6)
    root.right.right = BinarySearchTree(3)

    print(isSumTree(root))

main()
    
