from collections import defaultdict
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

def Top_view(root):
    if root is None:
        return

    view = []
    queue = []
    queue.append(root)
    hd = 0
    view.append([hd,root.data])
    
    i = 0
    while len(queue) > 0:
        #print(queue[0].data)
        node = queue.pop(0)
        print(i)
        if node.left is not None:
            queue.append(node.left)
            hd = view[i][0] - 1
            print(hd,root.left.data)
            if hd not in (item[0] for item in view):
                view.append([hd,node.left.data])
                
            
        if node.right is not None:
            queue.append(node.right)
            hd = view[i][0] + 1
            print(hd,root.right.data)
            if hd not in (item[0] for item in view):
                view.append([hd,node.right.data])
        
        if node.left is not None or node.right is not None:
            i += 1
    print(view)
        
    

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)

    #root.print_tree()
    Top_view(root)


main()
