def palindrome(string,start,end):
    
    while start < end:
        if string[start] != string[end]:
            return(False)
        start += 1
        end -= 1
        
    return(True)
    
    


def helper(string):
    temp = set()
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if palindrome(string,i,j) == True:
                temp.add(string[i:j])
    print(temp)
                


def main():
    string = str(input("Please enter the string: "))
    helper(string)


main()
