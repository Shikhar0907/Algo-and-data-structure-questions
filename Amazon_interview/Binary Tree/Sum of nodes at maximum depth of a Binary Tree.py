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

def Nodes(root):
    temp = 0
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].data)
        node = queue.pop(0)
        if node.left is None and node.right is None:
            temp = temp + node.data
        if node.left is not None:
            #print(node.left.data)
            queue.append(node.left)
        if node.right is not None:
            #print(node.right.data)
            queue.append(node.right)
        #print(queue)
    return(temp)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    #root.print_tree()

    print(Nodes(root))
    
main()
