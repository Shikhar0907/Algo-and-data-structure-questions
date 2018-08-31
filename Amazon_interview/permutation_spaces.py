def tostring(List):
    s = ''
    for x in List:
        if x == '\0':
            break
        s += x
    return(s)

def printpatternUtil(string,buff,i,j,n):
    if i == n:
        buff[j] = '\0'
        print(tostring(buff))
        return
    buff[j] = string[i]
    printpatternUtil(string,buff,i+1,j+1,n)

    buff[j] = " "
    printpatternUtil(string,buff,i+1,j+2,n)


def print_pattern(string):
    n = len(string)
    buff = [0] * (2*len(string))

    buff[0] = string[0]
    printpatternUtil(string,buff,1,1,n)


def main():
    string = str(input("Please enter the string: "))
    print_pattern(string)


main()
    
