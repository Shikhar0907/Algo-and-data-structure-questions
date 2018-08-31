def checkPalindrome(string):
    string = string.lower()
    start = 0
    end = len(string)-1
    while start < end:
        if string[start] != string[end]:
            return(False)
        start += 1
        end -= 1
    return(True)

def palindrome(string):
    count = 0
    arr = string.split()
    for item in arr:
        if checkPalindrome(item) == True:
            count += 1
    
    print(count)


def main():
    string = str(input("Please enter the string: "))
    palindrome(string)


main()
