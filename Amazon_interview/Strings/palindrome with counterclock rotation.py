def palindrome(string):
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return(False)
        left += 1
        right -= 1
    return(True)

def rotate(string):
    temp = list(string)
    first = temp[0]
    for i in range(len(temp)-1):
        temp[i] = temp[i+1]
    temp[-1] = first
    return(''.join(temp))
        


def rotation(string):
    count = 0
    while(True):
        if palindrome(string) == True:
            print(count)
            return(False)
        else:
            count += 1
            string = rotate(string)
    



def main():
    string = str(input("Please enter the string: "))
    if rotation(string) == False:
        print("yes")
    else:
        print("No")


main()
