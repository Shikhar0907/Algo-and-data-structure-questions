def zigzag(arr):
    flag = True
    for i in range(len(arr)-1):
        if flag == True:
            if arr[i] > arr[i+1]:

                arr[i],arr[i+1] = arr[i+1],arr[i]
        else:
            if arr[i] < arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

        flag = bool(1-flag)

    print(arr)




def main():
    arr = [4, 3, 7, 8, 6, 2, 1]
    zigzag(arr)

main()
