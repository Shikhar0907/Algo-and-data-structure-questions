def minRemoval(string):
    temp = [0] * 26
    for i in range(len(string)):
        temp[ord(string[i]) - ord('a')] += 1

    count = 0
    for i in range(len(temp)):
        if temp[i]%2 != 0 :
            count += 1

    return(count-1)




def main():
    string = str(input("Please enter the string: "))
    print(minRemoval(string))


main()
