def fixed_point(arr):
    for i in range(len(arr)):
        if arr[i] ==  i:
            print(arr[i],i)

def main():

    arr = list(map(int,input("Please enter the elements: ").split()))
    fixed_point(arr)


main()
