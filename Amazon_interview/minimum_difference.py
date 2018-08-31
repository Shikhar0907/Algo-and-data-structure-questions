def mini_difference(arr):
    mini = 12314
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] < mini:
            mini = arr[i+1] - arr[i]

    print(mini)


def main():
    arr = list(map(int,input("Please enter the elements: ").split()))
    mini_difference(arr)


main()
