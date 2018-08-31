def missing_number(arr):
    n = len(arr)
    total = ((n+1)*(n+2))/2
    Sum = sum(arr)
    print(total-Sum)

def main():
    arr = [1, 2, 4,6, 3, 7, 8]
    missing_number(arr)

main()
