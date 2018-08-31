def find_set(num):
    if (num+1) & num == 0:
        return(True)
    return(False)



def main():
    num = int(input("Please enter the number: "))
    print(find_set(num))


main()
