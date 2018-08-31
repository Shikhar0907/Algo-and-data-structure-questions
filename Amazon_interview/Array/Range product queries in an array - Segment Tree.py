def queries(arr,q):
    low,high = q[0],q[1]
    temp = []
    prod = 1
    for item in arr:
        prod = prod * item
        temp.append(prod)
    print(low,high)
    return(temp[high-1]/temp[low-2])
    




def main():
    arr = [5,10,15,20,25]
    q = [3,5]
    print(queries(arr,q))


main()
