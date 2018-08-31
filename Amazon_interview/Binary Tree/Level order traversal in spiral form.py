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

def traversal(root):
    if root is None:
        return
    queue1 = []
    queue1.append(root)
    queue2 = [] 
    while len(queue1) != 0 or len(queue2) != 0:
        while len(queue1) != 0:
            temp = queue1.pop(0)
            print(temp.data)
            if temp.right is not None:
                queue2.append(temp.right)
            if temp.left is not None:
                queue2.append(temp.left)
        while len(queue2) != 0:
            temp = queue2.pop(0)
            print(temp.data)
            if temp.left is not None:
                queue1.append(temp.left)
            if temp.right is not None:
                queue1.append(temp.right)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)

    traversal(root)

main()
