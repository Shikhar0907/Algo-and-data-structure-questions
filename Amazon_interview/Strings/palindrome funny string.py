def funny_word(string,new_string):
    
    string = string.lower()
    new_string = new_string.lower()
    for i in range(len(string)-1):
        diff1 = abs(ord(string[i])- ord(string[i+1]))
        diff2 = abs(ord(new_string[i]) - ord(new_string[i+1]))
        if diff1 != diff2:
            return(False)
    return(True)
        
    



def check(string):
    new_string = string[::-1]
    print(funny_word(string,new_string))


def main():
    string = str(input("Please enter the string: "))
    check(string)



main()
