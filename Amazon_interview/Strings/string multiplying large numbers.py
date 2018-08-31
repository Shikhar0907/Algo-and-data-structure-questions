def multiplying(string1,string2):
    l1 = len(string1)-1
    l2 = len(string2)-1
    mul = 0
    num = 0
    arr = []
    for i in range(len(string2)):
        num = int(string2)%10
        arr.append(num*(10**i))
        string2 = str(int(string2)//10)

    for item in arr:
        mul += item * int(string1)
    print(mul)
        
        




def main():
    string1 = str(input("Please enter the string1: "))
    string2 = str(input("Please enter the string2: "))
    multiplying(string1,string2)


main()
