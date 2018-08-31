def palindrome(string):
    l = 0
    r = len(string)-1
    while l < r:
        if string[l] != string[r]:
            return(False)
        l += 1
        r -= 1
    return(True)



def main():
    string = str(input("Please enter the string: "))
    print(palindrome(string))



main()
