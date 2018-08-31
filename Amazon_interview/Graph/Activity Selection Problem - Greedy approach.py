class Activity:
    def __init__(self):
        self.queue = []
        

    def insert(self,start,finish):
        self.queue.append([start,finish])

    def printMaxActivity(self,arr,n):
        arr = sorted(arr,key=lambda x:x[1])
        print(arr[0])
        i = 0
        for j in range(1,len(arr)):
            if arr[j][0] > arr[i][1]:
                print(arr[j])
                i = j
        



def main():
    root = Activity()
    root.insert(5,9)
    root.insert(1,2)
    root.insert(3,4)
    root.insert(0,6)
    root.insert(5,7)
    root.insert(8,9)

    print(root.queue)
    root.printMaxActivity(root.queue,len(root.queue))


    
main()
