def convert(x):
    a = bin(x)
    for i in range(len(a)-1,0,-1):
        print(i,a[i])
        if a[i] == '1':
            return(i)


def main():
    x = int(input("Please enter the element: "))
    print(convert(x))


main()
