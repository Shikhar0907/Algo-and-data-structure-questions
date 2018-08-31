def remove_n_digits(arr,n,res):
    if n ==0:
        res = res + arr
        return
    l = len(arr)
    if len(arr) <= n:
        return
    min_point = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_point]:
            min_point = i
    res = res+arr[min_point]
    new_str = arr[min_point+1:l-min_point]

    remove_n_digits(new_str,n-min_point,res)
        



def main():
    string = str(input("Please enter the elements: "))
    res = ""
    n = 3
    print(remove_n_digits(string,n,res))
    print(res)


main()
