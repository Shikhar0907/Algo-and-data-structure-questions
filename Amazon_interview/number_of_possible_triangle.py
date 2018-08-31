def triangles(arr):
    count = 0
    arr.sort()
    for i in range(len(arr)-2):
        k = i+2
        for j in range(i+1,len(arr)):
            while k < len(arr) and arr[i] + arr[j] > arr[k]:
                k += 1
            count += k - j -1
    print(count)
            
            


def main():
    arr = list(map(int,input("Please enter the elements: ").split()))
    triangles(arr)


main()
