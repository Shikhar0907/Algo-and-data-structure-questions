def pythagorean(arr):
    arr.sort()
    temp = 0
    for i in range(len(arr)):
        arr[i] = arr[i]**2
    for i in range(len(arr)-2):
        temp = arr[i] + arr[i+1]
        if temp in arr:
            print("True")
            break
        


def main():
    arr = [3,1,4,6,5]
    pythagorean(arr)


main()
