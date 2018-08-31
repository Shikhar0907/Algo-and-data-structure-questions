def mini_num(arr,n,res):
    if len(arr) < n:
        return
    if n == 0:
        res = res + arr
        return
    min_pt = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_pt]:
            min_pt = i
    res = res + arr[min_pt]
    new_str = arr[min_pt]
    mini_num(new_str,n-min_pt,res)




def main():
    arr = "523460"
    n = 3
    res = ""
    mini_num(arr,n,res)
    print(res)

main()
