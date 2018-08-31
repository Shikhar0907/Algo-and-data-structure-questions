def longest_substring(string):
    max_length = 0
    for i in range(len(string)):
        max_length = max(max_length, helper(string,i))
    return(max_length)



def helper(string,start):
    seen = set()
    for i in range(start,len(string)):
        if string[i] not in seen:
            seen.add(string[i])
        else:
            return(i-start)
    return(len(string) - start)

def main():
    string = str(input("Please enter the string: "))
    print(longest_substring(string))


main()
