class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data is not None:
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                print("Already Present")

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

def traversal(root,point):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) != 0:
        if queue[0].data == point:
            print(queue[0].data)
            break
        print(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    

      
def main():
    arr = list(map(int,input("Please enter the elements : ").split()))

    for i in range(len(arr)):
        if i == 0:
            root = Node(arr[i])
        else:
            root.insert(arr[i])

    #root.print_tree()
    traversal(root,15)
    
main()
