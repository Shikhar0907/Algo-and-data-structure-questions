def replace_right(arr):
    max_right = arr[len(arr)-1]
    arr[-1] = -1
    
    for i in range(len(arr)-2,-1,-1):
        temp = arr[i]

        arr[i] = max_right
        if max_right < temp:
            max_right = temp

    print(arr)




def main():
    arr = [16,17,4,3,5,2]
    replace_right(arr)


main()
