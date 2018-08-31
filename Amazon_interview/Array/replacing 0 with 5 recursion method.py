def replacing(arr):
    if arr == 0:
        return(0)
    digit = arr%10
    
    if digit == 0:
        digit = 5
    return(replacing(int(arr/10))*10 + digit)


def main():
    arr = int(input("Please enter the integer: "))
    print(replacing(arr))

main()
    
