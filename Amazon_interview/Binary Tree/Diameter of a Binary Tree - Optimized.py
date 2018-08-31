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

def diameter(root,height):
    if root is None:
        height = 0
        return(height)
    left_height = 0
    right_height = 0

    left_diameter = 0
    right_diameter = 0

    left_diameter = diameter(root.left,left_height)
    right_diameter = diameter(root.right,right_height)

    height = 1+max(left_height,right_height)
    return(max((left_height+right_height+1),max(left_diameter,right_diameter)))
    


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root.print_tree()
    height = 0
    print(diameter(root,height))

main()
