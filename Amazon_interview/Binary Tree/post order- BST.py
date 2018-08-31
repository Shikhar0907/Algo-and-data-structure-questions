class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self,data):
        if self.data:
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
                print("already present")

        else:
            self.data = Node(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        print(self.data)

def main():
    arr = list(map(int,input("please enter the elements:").split()))
    for i in range(len(arr)):
        if i == 0:
            root = Node(arr[i])
        else:
            root.insert(arr[i])

    root.print_tree()


main()
    
