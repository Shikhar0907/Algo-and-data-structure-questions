def missing_num(arr):
    n = len(arr)
    total = (n+1) * (n+2)/2
    for item in arr:
        total -= item
    print(total)



def main():
    arr = [1,2,4,6,3,7,8]
    missing_num(arr)

main()
