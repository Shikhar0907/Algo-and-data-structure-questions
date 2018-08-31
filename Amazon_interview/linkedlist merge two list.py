class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def create(self):
        elements = list(map(int,input("Please enter the elements: ").split()))
        for item in elements:
            self.insert(item)


    def insert(self,data):
        temp = Node(data)
        while self.start is None:
            self.start = temp
            return
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp


    def print_list(self):
        p = self.start
        while p.next is not None:
            print(p.data,end="->")
            p = p.next
        print(p.data)

def merge_list(root,start):
    temp = None
    if start is None:
        return(start)
    if root is None:
        return(root)
    
    if root.data <= start.data:
        temp = root
        temp.next = merge_list(root.next,start)
    else:
        temp  = start
        temp.next = merge_list(root,start.next)

    return(temp)
        

def main():
    root = LinkedList()
    root.create()
    

    head = LinkedList()
    head.create()
    root.print_list()
    head.print_list()

    temp= LinkedList()
    temp.start = merge_list(root.start,head.start)
    temp.print_list()

main()
