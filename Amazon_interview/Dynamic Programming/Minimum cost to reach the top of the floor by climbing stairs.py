def cost(arr):
    temp = [0] * len(arr)
    temp[0] = arr[0]
    temp[1] = arr[1]

    for i in range(2,len(arr)):
        temp[i] = min(temp[i-1],temp[i-2])+arr[i]
    print(min(temp[len(temp)-1],temp[len(temp)-2]))
    

def main():
    arr = [16,19,10,12,18]
    cost(arr)


main()
