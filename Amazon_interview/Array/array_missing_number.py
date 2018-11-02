def missing_number(arr):
    n = len(arr)
    total = ((n+1)*(n+2))/2
    Sum = sum(arr)
    return(int(total-Sum))

def main():
    arr = [1, 2,3,5,6]
    print(missing_number(arr))

main()
