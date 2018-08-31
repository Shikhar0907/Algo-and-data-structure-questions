class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def create_list(self):
        elements = list(map(int,input("Please enter the elements: ").split()))
        for item in elements:
            self.insert(item)


    def insert(self,data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp

    def print_linkedlist(self):
        p = self.start
        while p.next is not None:
            print(p.data)
            p = p.next
        print(p.data)

    def delete_nodes(self,n,m):
        cur_ptr = self.start
        fast_ptr = self.start
        count = 0
        while count < m-1:
            cur_ptr = cur_ptr.next
            fast_ptr = fast_ptr.next
            count += 1
        count =0
        while count < n+1:
            fast_ptr = fast_ptr.next
            count += 1
        cur_ptr.next = fast_ptr
        

        
        
        
            
def main():
    root = LinkedList()
    root.create_list()
    root.print_linkedlist()
    n = 2
    m = 3
    root.delete_nodes(n,m)
    root.print_linkedlist()

main()
