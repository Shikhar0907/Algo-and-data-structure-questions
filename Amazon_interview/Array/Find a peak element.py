def find_peak(arr,low,high,n):
    mid = int(low + (high-low)/2)
    if ((mid ==0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1] <= arr[mid])):
        return(mid)

    elif mid > 0 and arr[mid-1] > arr[mid]:
        return(find_peak(arr,low,mid-1,n))
    else:
        return(find_peak(arr,mid+1,high,n))



def main():
    arr = [1,3,20,4,1,0]
    print(find_peak(arr,0,len(arr)-1,len(arr)))


main()
