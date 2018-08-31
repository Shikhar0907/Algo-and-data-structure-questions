def search(arr,low,high):
    if low > high:
        return(None)
    if low== high:
        return(arr[low])
    mid = int(low + (high-low)/2)

    if mid%2 == 0:
        if arr[mid] == arr[mid+1]:
            return(search(arr,mid+2,high))
        else:
            return(search(arr,low,mid))
    else:
        if arr[mid] == arr[mid-1]:
            return(search(arr,mid+1,high))
        else:
            return(search(arr,low,mid-1))



def main():
    arr = [1,1,2,4,4,5,5,6,6]
    print(search(arr,0,len(arr)-1))

main()
