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

def findpath(root,path,k):
    if root is None:
        return(False)
    path.append(root.data)
    if root.data == k:
        return(True)
    if ((root.left != None and findpath(root.left,path,k)) or (root.right != None and findpath(root.right,path,k))):
        return(True)
    

    path.pop()
    return(False)

def findDistance(root,num,dist):
    if root is None:
        return(0)
    dist = findDistance(root.left,num,dist)
    dist = findDistance(root.right,num,dist)

    if root.data == num:
        return(True)
    return(dist+1)


def findLCA(root,num1,num2):
    path1 = []
    path2 = []

    if (not findpath(root,path1,num1) or (not findpath(root,path2,num2))):
        return -1
    print(path1,path2)
    
    dist1 = findDistance(root,num1,0)
    dist2 = findDistance(root,num2,0)
    i = 0
    while i< len(path1) and i < len(path2) :
        if path1[i] != path2[i]:
            break
        i += 1
    return(dist1+ dist2 - 2*i)

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    #root.print_tree()
    print(findLCA(root,4,5))
    
        
main()
