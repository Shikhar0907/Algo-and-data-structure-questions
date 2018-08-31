def product(arr,x):
    temp = set(arr)
    div = 0
    for item in arr:
        div = int(x/item)
        
        if div in list(temp):
            
            return(True)
        
    
    return(False)



def main():
    arr = list(map(int,input("Please enter the elements: ").split()))
    x = int(input("Please enter the element: "))
    if (product(arr,x)) == True:
        print("Yes")
    else:
        print("No")


main()
