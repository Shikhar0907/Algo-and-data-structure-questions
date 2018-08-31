def triplet(arr,num):
    arr.sort()
    ans = 0
    for i in range(0, len(arr)-2):
        j = i-1
        k = len(arr)-1
        while j < k:
            if arr[i] + arr[j] + arr[k] >= num:
                k -= 1
            else:
                ans += 1
                #print(ans)
                j += 1

    return(ans)
    


def main():
    arr = list(map(int,input("Please enter the elements: ").split()))
    num = int(input("Please eneter the number: "))
    print(triplet(arr,num))


main()
