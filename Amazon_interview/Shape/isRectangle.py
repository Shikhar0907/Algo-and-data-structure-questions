def dist(point1,point2):
    return((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def isRectangle(arr):
    rect = []
    for i in range(len(arr)):
        for j in range(0,len(arr[0]),2):
            temp = [arr[i][j],arr[i][j+1]]
            if temp not in rect:
                rect.append(temp)
    print(rect)
    if len(rect) != 4:
        return(False)

    distance = []
    for i in range(len(rect)):
        for j in range(i+1,len(rect)):
            print(rect[i],rect[j])
            distance.append(dist(rect[i],rect[j]))
    distance = set(distance)
    print(distance)
    return(list(distance)[0] + list(distance)[1] == list(distance)[2])


def main():
    arr = [[4,2,7,5],[2,4,4,2],[2,4,5,7],[5,7,7,5]]
    print(isRectangle(arr))


main()
