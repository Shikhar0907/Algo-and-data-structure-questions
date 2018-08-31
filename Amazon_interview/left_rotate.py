def left_rotation(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]

    arr[len(arr)-1] = temp
        


def array_rotation(arr,pos):
    for i in range(pos):
        left_rotation(arr)
    print(arr)


def main():
    arr = list(map(int,input("Please enter the array: ").split()))
    pos = int(input("Please enter the rotation: "))
    (array_rotation(arr,pos))


main()
