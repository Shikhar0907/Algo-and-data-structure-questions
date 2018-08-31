def equilibrium(arr):
    total = sum(arr)
    num = 0
    for i in range(len(arr)):
        total -= arr[i]
        if total == num:
            print(i)
            break
        num += arr[i]
        print(total,num)
            



def main():
    arr = [-7, 1, 5, 2, -4, 3, 6]
    equilibrium(arr)

main()
