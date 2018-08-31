def max_multiplication(arr):
    arr.sort()
    return(arr[-1],arr[-2])



def main():
    arr = [1,4,3,6,7,0]
    print(max_multiplication(arr))


main()
