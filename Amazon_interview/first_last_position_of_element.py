def occurrence(arr,num):
    i = 0
    j = len(arr)-1
    while i < len(arr)-1:
        if arr[i] == num:
            break
        i += 1
        
    while j >= 0:
        if arr[j] == num:
            break
        j -= 1
    print(i,j)
        
        

def main():
    arr = list(map(int,input("Please enter the elements: ").split()))
    num = int(input("Please enter the number: "))
    
    occurrence(arr,num)


main()
