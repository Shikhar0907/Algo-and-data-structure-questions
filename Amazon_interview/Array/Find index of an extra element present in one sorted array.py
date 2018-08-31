def extra_element(arr1,arr2):
    index = 0

    left = 0
    right = len(arr2)-1

    while left < right:
        mid = int(left + (right-left)/2)

        if arr1[mid] == arr2[mid]:
            left = mid+1

        else:
            index = mid
            right = mid-1

    return(index)





def main():
    arr1 = [2,4,6,8,9,10,12]
    arr2 = [2,4,6,8,10,12]

    print(extra_element(arr1,arr2))


main()
