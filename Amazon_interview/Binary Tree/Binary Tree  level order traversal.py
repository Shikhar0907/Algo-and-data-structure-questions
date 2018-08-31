class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def main():
    root = Node(10)
    root.left = Node(6)
    root.left.left = Node(4)
    root.left.right = Node(8)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(16)

    level_order(root)


main()
