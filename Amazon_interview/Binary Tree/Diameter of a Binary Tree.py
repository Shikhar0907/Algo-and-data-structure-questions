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

def height(root):
    if root is None:
        return(0)
    return(1+ max(height(root.left),height(root.right)))

def diameter(root):
    if root is None:
        return(0)
    left_height = height(root.left)
    right_height = height(root.right)
    
    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)
    print(root.data,left_diameter,right_diameter)
    print(left_height,right_height)

    return(max(left_height + right_height + 1, max(left_diameter, right_diameter)))

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    #root.print_tree()
    print(diameter(root))

main()
