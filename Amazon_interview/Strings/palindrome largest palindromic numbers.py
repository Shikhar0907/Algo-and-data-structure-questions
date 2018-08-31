test = []

def palindromic_number(string):
    start = 0
    end = len(string)-1
    while start < end:
        if string[start] != string[end]:
            return(False)
        start += 1
        end -= 1
    return(True)
        


def tostring(string):
    return(''.join(string))

def permutation(string,l,h):
    
    if l == h:
        temp = (tostring(string))
        if palindromic_number(temp) == True:
            test.append(temp)
        
            
    else:
        for i in range(l,h+1):
            string[i],string[l] = string[l],string[i]
            permutation(string,l+1,h)
            string[i],string[l] = string[l],string[i]
            
    



def main():
    string = str(input("Please enter the string: "))
    string = list(string)
    low = 0
    high = len(string)-1
    permutation(string,low,high)
    print(test)

main()
