def dist(point1, point2):
    return((point1[0]- point2[0])**2 + (point1[1] - point2[1])**2)


def isSquare(point1,point2,point3,point4):
    d1 = dist(point1,point2)
    d2 = dist(point1,point3)
    d3 = dist(point1,point4)

    if d1 == d2 and 2*d1 == d3:
        d = dist(point2,point4)
        return(d == dist(point3, point4) and d == d1)
    if d2 == d3 and d1 == 2*d2:
        d = dist(point2,point3)
        return(d == dist(point2,point4) and d == d2)
    if d1 == d3 and 2*d1 == d2:
        d = dist(point2,point3)
        return( d == dist(point3,point3) and d == d1)
    return(False)

def main():
    point1 = [20,10]
    point2 = [10,20]
    point3 = [20,20]
    point4 = [10,10]

    print(isSquare(point1,point2,point3,point4))
main()
