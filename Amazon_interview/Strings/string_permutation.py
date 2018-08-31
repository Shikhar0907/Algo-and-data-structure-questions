def tostring(string):
    return(''.join(string))


def permute(string,l,h):
    if l == h:
        print(tostring(string))
    else:
        for i in range(l,h+1):
            string[i],string[l] = string[l],string[i]
            permute(string,l+1,h)
            string[i],string[l] = string[l],string[i]
            


def main():
    string = str(input("Please enter the string: "))
    l = 0
    h = len(string)-1
    string = list(string)
    permute(string,l,h)


main()
