def Area(x1,y1,x2,y2,x3,y3):
    return(abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)



def isInside(x1,y1,x2,y2,x3,y3,x,y):
    A = Area(x1,y1,x2,y2,x3,y3)
    A1 = Area(x,y,x2,y2,x3,y3)
    A2 = Area(x1,y1,x,y,x3,y3)
    A3 = Area(x1,y1,x2,y2,x,y)

    return(A == A1+A2+A3)
        



def main():
    print(isInside(0,0,20,0,10,30,10,15))

main()
    
