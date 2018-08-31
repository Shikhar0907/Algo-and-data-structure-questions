def smaller_number(arr):
    print("_,", end="")
    for i in range(1,len(arr)):
        for j in range(i-1,-2,-1):
            if (arr[j] < arr[i]):
                print(arr[j],",",end="")
                break
            if j == -1:
                print("_,",end="")
            



def main():
    arr = list(map(int,input("Please enter the elements: ").split()))
    smaller_number(arr)


main()
