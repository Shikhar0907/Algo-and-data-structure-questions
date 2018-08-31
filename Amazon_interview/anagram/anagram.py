def anagram(string1,string2):
    count = 0
    for item in string1:
        if item in string2:
            count += 1
    if count == len(string1):
        return(True)
    else:
        return(False)




def main():
    string1 = str(input("Please enter the string: "))
    string2 = str(input("Please enter the string: "))
    if anagram(string1,string2) == True:
        print("Yes")
    else:
        print("No")


main()
