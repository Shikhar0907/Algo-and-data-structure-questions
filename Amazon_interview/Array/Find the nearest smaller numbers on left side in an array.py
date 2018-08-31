def find_left(arr):
    print("_,",end=" ")
    
    for i in range(1,len(arr)):
        for j in range(i-1,-2,-1):
            if arr[j] < arr[i]:
                print("%d, "%arr[j],end="")
                break
        if j == -1:
            print("_, ", end="")
        

def main():
    arr = [1,6,4,10,2,5]
    find_left(arr)

main()
