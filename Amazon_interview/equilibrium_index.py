def equilibrium(arr):
    total = sum(arr)
    leftsum = 0
    for i,num in enumerate(arr):
        total = total - num
        if leftsum == total:
            return(i)
        leftsum = leftsum + num
    return(-1)
        



def main():
    arr = list(map(int,input("Please enter the elements: ").split()))
    print(equilibrium(arr))


main()
