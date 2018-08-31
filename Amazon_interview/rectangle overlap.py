class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def isOverlap(l1,r1,l2,r2):
    if l1.x > r2.x or l2.x > r1.x:
        return(False)
    if l1.y < r2.y or l2.y < r1.y:
        return(False)
    return(True)

def main():
    l1 = Point(1,8)
    r1 = Point(4,4)
    l2 = Point(5,5)
    r2 = Point(9,1)
    if (isOverlap(l1,r1,l2,r2)) == True:
        print("Yes")
    else:
        print("No")

main()
