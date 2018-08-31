def distsq(p,q):
    x1,y1 = p
    print(x1,y1)
    x2,y2 = q
    print(x2,y2)
    return(((x1 -x2)**2) + ((y1-y2)**2))

def isSquare(p1,p2,p3,p4):
    d2 = distsq(p1,p2)
    d3 = distsq(p1,p3)
    d4 = distsq(p1,p4)
    if (d2 == d3 and 2*d2 == d4):
        d = distsq(p2,p4)
        return(d == distsq(p3,p4) and d == d2)
    if d3 == d4 and 2*d2 == d4:
        d = distsq(p2,p4)
        return(d == distsq(p3,p4) and d ==d2)
    if d2 == d4 and 2*d2 == d3:
        d = distsq(p2,p3)
        return(d == distsq(p3,p4) and d ==d2)
    return(False)



def main():
    point1 = (20,10)
    point2 = (10,20)
    point3 = (20,20)
    point4 = (10,10)
    
    if isSquare(point1,point2,point3,point4):
        print("Yes")
    else:
        print("No")


main()
