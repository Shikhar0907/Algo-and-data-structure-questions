def prev_greater_element(arr):
    temp = []
    temp.append(arr[0])
    print("-1")
    for i in range(1,len(arr)):
        while len(temp) != 0 and temp[-1] < arr[i]:
            temp.pop()
        if len(temp)!= 0:
            if temp[-1] > arr[i]:
                print(temp[-1])
        elif len(temp) == 0:
            print("-1")
        temp.append(arr[i])
                
                

def main():
    arr = list(map(int,input("Please enter the elements: ").split()))
    prev_greater_element(arr)

main()
