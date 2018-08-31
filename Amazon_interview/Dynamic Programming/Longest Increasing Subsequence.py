def LIS(arr):
    length = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(0,i):
            if arr[i] > arr[j]:
                
                length[i] = max(length[j]+1,length[i])

    print(length)


def main():
    arr = [0,4,12,2,10,6,9,13,3,11,7,15]
    LIS(arr)

main()
