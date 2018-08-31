def palindrome(string):
    temp = [0] * 256
    for i in range(len(string)):
        temp[ord(string[i])] = temp[ord(string[i])] + 1

    odd = 0
    for i in range(0,256):
        if temp[i] & 1:
            odd += 1

        if odd > 1:
            return(False)
    return(True)



def main():
    string = str(input("Please enter the string: "))
    if palindrome(string) == True:
        print("Yess")
    else:
        print("Nooo")

main()
